n = int(input())


def fibo(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10007
    return a


print(fibo(n))
