def is_odd(n):
    return n % 2 == 1


print(list(filter(lambda n: n % 2 == 1, range(1, 20))))