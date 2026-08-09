## functions/arguments
#Sum
def new(*args):
    print("Arguments passed to the function:", args)
    return sum(args)

print(new(1, 2, 3, 4, 5))

#Average
def avg(*args):
    print("Arguments passed to the function:", args)
    return sum(args) / len(args)

print(avg(1, 2, 3, 4, 5))

def maximum(*args):
    print("Arguments passed to the function:", args)
    return max(args)

print(maximum(1, 2, 3, 4, 5))

# Generator function to yield squares of numbers
def square_generator(n):
    for i in range(n):
        yield i * i

for square in square_generator(10):
    print(square)

# Decorators
def decorator(func):
    def wrapper():
        print("Before executing the function.",func.__name__)
        func()
        print("After executing the function.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


# Closure
def power(n):
    def n_power(x):
        return x**n
    return n_power

square = power(2)
cube = power(3)

print(square(5))
print(cube(5))

# data class
from dataclasses import dataclass

@dataclass
class Employee:
    id : int
    name : str
    department : str
    salary : float

print(Employee(1, "John Doe", "IT", 50000.0))