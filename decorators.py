def my_decorator(func):
    def wrapper():
        print("Something happens before the function is called.")
        func()
        print("Something happens after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


import time

def execution_time(func):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution Time: {end-start:.6f} seconds")

        return result

    return wrapper

@execution_time
def calculate():

    total = 0

    for i in range(1000000):
        total += i

    return total

calculate()