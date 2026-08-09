def main_func(a):
    b = 10
    def inner_func(c):
        return a * b *c
    return inner_func

times_10 = main_func(10)
result = times_10(5)
print(result)