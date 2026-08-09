def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

@decorator
def get_time():
    import time
    return time.ctime()

get_time()