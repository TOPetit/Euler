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