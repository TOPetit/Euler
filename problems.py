import math


def solve1():
    res = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    print(res)


def solve2():
    res = 0
    n = 1
    m = 1
    while n <= 4000000:
        mem = n
        n = m
        m = mem + n
        if n % 2 == 0:
            res += n
    print(res)


def solve3():
    n = 600851475143
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    print(n)


def solve4():
    res = 0
    for i in range(1000):
        for j in range(1000):
            n = i * j
            if res < n:
                l = [int(x) for x in str(n)]
                if l == l[::-1]:
                    res = n
    print(res)


def solve5():
    def is_ok(k):
        n = 20
        i = 1
        while i < n and k % i == 0:
            i += 1
        return k % i == 0

    k = 2
    while not is_ok(k):
        k += 2
    print(k)


def solve6():
    n = 100
    sum_of_sq = 0
    sq_of_sum = 0
    for i in range(n):
        sum_of_sq += (i + 1) ** 2
        sq_of_sum += i + 1
    print(sq_of_sum ** 2 - sum_of_sq)


def solve7():
    n = 10001
    i = 1
    num = 1
    value = 0
    while i < n:
        num += 2
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            value = num
            i += 1
    print(value)
