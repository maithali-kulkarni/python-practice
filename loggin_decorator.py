def decorator(func):
    def wrapper(a,b):
        print("Calling function", {func.__name__})
        print("Arguments are", a, b)
        return func(a, b)
    return wrapper

@decorator
def add(a, b):
    print("Return:",a+b)
    return a+b

add(2,3)