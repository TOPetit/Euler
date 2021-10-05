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


def solve8():
    n = 13
    l = []
    f = open("sources/problem8.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        for num in line:
            try:
                l.append(int(num))
            except:
                pass
    nb_num = len(l)
    maxi = 0
    for i in range(0, nb_num - n):
        maxi = max(maxi, math.prod(l[i : i + n]))
    print(maxi)


def solve9():
    # hypothenuse
    x, y, z = 0, 0, 0
    for a in range(334, 999):
        for b in range(1, 999 - a):
            c = 1000 - b - a
            if a ** 2 == b ** 2 + c ** 2:
                x, y, z = a, b, c
    print(x * y * z)


def solve10():
    n = 2000000
    value = 2
    for num in range(3, n, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            value += num
    print(value)


def solve11():
    k = 4
    f = open("sources/problem11.txt", "r")
    lines = f.readlines()
    f.close()
    l = [[] for i in range(len(lines))]
    i = 0
    for line in lines:
        try:
            l[i] = line.strip().split(" ")
            l[i] = list(map(int, l[i]))
        except:
            pass
        i += 1
    n = len(l)
    m = len(l[0])
    maxi = 0
    for x in range(n - k + 1):
        for y in range(m - k + 1):
            horizontal = 1
            vertical = 1
            diagonal1 = 1
            diagonal2 = 1
            for p in range(k):
                horizontal *= l[x][y + p]
                vertical *= l[x + p][y]
                diagonal1 *= l[x + p][y + p]
                diagonal2 *= l[x + k - p - 1][y + p]
            maxi = max(maxi, horizontal)
            maxi = max(maxi, vertical)
            maxi = max(maxi, diagonal1)
            maxi = max(maxi, diagonal2)
    print(maxi)


def solve12():
    q = 500
    k = 0
    n = 1

    def countDivisors(n):
        cnt = 0
        for i in range(1, (int)(math.sqrt(n)) + 1):
            if n % i == 0:
                if n / i == i:
                    cnt = cnt + 1
                else:
                    cnt = cnt + 2
        return cnt

    while countDivisors(k) < q:
        k = n * (n + 1) // 2
        n += 1
    print(k)


def solve13():
    d = 10
    f = open("sources/problem13.txt", "r")
    lines = f.readlines()
    f.close()
    res = 0
    for i in range(len(lines)):
        res += int(lines[i][: 2 * d])  # Could give bad result
    print(str(res)[:d])


def solve14():
    def collatz(n, iter):
        if n % 2 == 0:
            return collatz(n // 2, iter + 1)
        else:
            if n == 1:
                return iter
            else:
                return collatz(3 * n + 1, iter + 1)

    n = 1000000
    maxi = 0
    mem = 0
    for i in range(1, n):
        chain = collatz(i, 1)
        if maxi < chain:
            # print("%d: %d" % (i, chain))
            mem = i
            maxi = chain
    print(mem)


def solve15():
    n = 20
    print(math.factorial(2 * n) // (math.factorial(n) ** 2))


def solve16():
    n = 2 ** 1000
    res = 0
    for digit in str(n):
        res += int(digit)
    print(res)


def solve17():
    n = 1000
    values = {
        "1": 1,
        "2": 3,
        "3": 5,
        "4": 4,
        "5": 4,
        "6": 3,
        "7": 5,
        "8": 5,
        "9": 4,
        "10": 3,
        "11": 6,
        "12": 6,
        "13": 8,
        "14": 8,
        "15": 7,
        "16": 7,
        "17": 9,
        "18": 8,
        "19": 9,
        "20": 6,
        "30": 6,
        "40": 6,
        "50": 5,
        "60": 5,
        "70": 7,
        "80": 6,
        "90": 6,
        "100": 7,
        "1000": 8,
        "and": 3,
        "plural": 1,
    }
    res = 0
    for i in range(1, n + 1):
        num_list = list(str(i))
        print(num_list)
        if len(num_list) == 4:
            res += values["1000"] + values["1"]
            num_list = []
            print(num_list)
        if len(num_list) == 3:
            if num_list[0] != "0":
                res += values["100"] + values[num_list[0]]
                if num_list[1:] != ["0", "0"]:
                    res += values["and"]
            num_list = num_list[1:]
            print(num_list)
        if len(num_list) == 2:
            if num_list[0] != "0":
                if num_list[0] == 1:
                    res += values["1" + num_list[1]]
                    num_list = []
                    print(num_list)
                else:
                    res += values[num_list[0] + "0"]
                    num_list = num_list[1:]
                    print(num_list)
            else:
                num_list = num_list[1:]
        if len(num_list) == 1:
            if num_list[0] != "0":
                res += values[num_list[0]]
    print(res)
