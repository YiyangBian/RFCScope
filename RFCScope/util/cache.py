import os
import inspect
import hashlib
import pickle
import shutil

# base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

def cache(*cache_keys, skip_args=None):
    """
    A decorator factory that caches the result of a function call.The cache is stored in f"{base_dir}/.cache/{hash}" where the
    hash is generated from the function definition and its arguments.
    
    Thus the cache is invalidated if the function definition or its arguments change.
    
    This works best for functions that are deterministic, have no side effects, and
    are not created dynamically (e.g., executed from a string).
    Further, the arguments and return values should be serializable.
    
    Additional cache_keys can be provided which will be included in the hash generation.
    
    Example:
        @cache("v1", some_variable)
        def my_function(x, y):
            return x + y

    `skip_args` is a list of argument names that should be skipped when generating the hash.
    This is useful when some arguments are not relevant for the cache key (or are not serializable).
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # generate a hash from the function definition, its arguments, and cache keys
            try:
                func_str = inspect.getsource(func)
            except Exception:
                func_str = str(func) # this cache will likely be invalidated after a restart
            
            # handle skip_args
            skip_list = skip_args or []
            param_names = list(inspect.signature(func).parameters.keys())

            # filter args based on skip_list
            filtered_args = [arg for i, arg in enumerate(args) if param_names[i] not in skip_list]
            
            # filter kwargs based on skip_list
            filtered_kwargs = {k: v for k, v in kwargs.items() if k not in skip_list}
            
            args_str = str(filtered_args)
            kwargs_str = str({k: filtered_kwargs[k] for k in sorted(filtered_kwargs)})
            
            # no cache keys if the decorator is used without parameters
            if len(cache_keys) == 1 and callable(cache_keys[0]):
                cache_keys_str = ""
            else:
                cache_keys_str = str(cache_keys)

            # generate the hash
            hash_str = hashlib.sha256(str((func_str, args_str, kwargs_str, cache_keys_str)).encode()).hexdigest()

            # check if the cache exists
            cache_path = os.path.join(base_dir, ".cache", hash_str)
            if os.path.exists(cache_path):
                with open(cache_path, "rb") as f:
                    return pickle.load(f)
            else:
                result = func(*args, **kwargs)
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                with open(cache_path, "wb") as f:
                    pickle.dump(result, f)
                return result
            
        return wrapper
    
    # Handle the case where the decorator is used without parameters
    if len(cache_keys) == 1 and callable(cache_keys[0]):
        return decorator(cache_keys[0])
    return decorator


def flush_cache():
    """
    Flushes the cache by deleting all cache files.
    """
    cache_dir = os.path.join(base_dir, ".cache")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
