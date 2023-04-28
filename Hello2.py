L = [x * x for x in range(10)]
print(L)

# 生成器 generator
g = (x * x for x in range(10))
print(g)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return "done"


print(next(fib(50)))
