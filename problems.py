import math
from datetime import date


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
        maxi = max(maxi, math.prod(l[i: i + n]))
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
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
        "20": "Twenty",
        "30": "Thirty",
        "40": "Forty",
        "50": "Fifty",
        "60": "Sixty",
        "70": "Seventy",
        "80": "Eighty",
        "90": "Ninety",
        "100": "Hundred",
        "1000": "Thousand",
        "and": "and",
    }
    res = 0
    for i in range(1, n + 1):
        tmp = ""
        num_list = list(str(i))
        # print(num_list)
        if len(num_list) == 4:
            tmp = values["1"] + values["1000"]
            num_list = []
            # print(num_list)
        if len(num_list) == 3:
            if num_list[0] != "0":
                tmp = tmp + values[num_list[0]] + values["100"]
                if num_list[1:] != ["0", "0"]:
                    tmp = tmp + values["and"]
            num_list = num_list[1:]
            # print(num_list)
        if len(num_list) == 2:
            if num_list[0] != "0":
                if num_list[0] == "1":
                    tmp = tmp + values["1" + num_list[1]]
                    num_list = []
                    # print(num_list)
                else:
                    tmp = tmp + values[num_list[0] + "0"]
                    num_list = num_list[1:]
                    # print(num_list)
            else:
                num_list = num_list[1:]
        if len(num_list) == 1:
            if num_list[0] != "0":
                tmp = tmp + values[num_list[0]]
        # print(tmp)
        res += len(tmp)
    print(res)


def solve18():
    f = open("sources/problem18.txt", "r")
    lines = f.readlines()
    f.close()
    mem = [[] for i in range(len(lines))]
    i = 0
    for line in lines:
        try:
            mem[i] = line.strip().split(" ")
            mem[i] = list(map(int, mem[i]))
        except:
            pass
        i += 1
    for i in range(len(mem) - 2, -1, -1):
        for j in range(len(mem[i])):
            mem[i][j] = max(mem[i + 1][j], mem[i + 1][j + 1]) + mem[i][j]
    print(mem[0][0])


def solve19():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                sundays += 1
    print(sundays)


def solve20():
    n = math.factorial(100)
    res = 0
    while n != 0:
        res += n % 10
        n = n // 10
    print(res)


def solve21():
    n = 10000
    divs = []
    res = 0
    for num in range(1, n + 1):
        count = 0
        for div in range(1, num):
            if num % div == 0:
                count += div
        divs.append(count)
    for i in range(1, n):
        j = divs[i-1]
        if j < n:
            if divs[j-1] == i and i != j:
                res += i
    print(res)


def solve22():
    f = open("sources/problem22.txt", 'r')
    lines = f.readline().replace('"', '').split(",")
    f.close()
    lines.sort()

    res = 0
    for i_name in range(len(lines)):
        score = 0
        for letter in lines[i_name]:
            score += 1 + ord(letter) - ord('A')
        res += score * (i_name + 1)
    print(res)


def solve23():
    n = 28124

    def getDivisors(num):
        if num == 1:
            return 1
        n = math.ceil(math.sqrt(num))
        total = 1
        divisor = 2
        while (divisor < n):
            if (num % divisor == 0):
                total += divisor
                total += num//divisor
            divisor += 1
        if n**2 == num:
            total += n
        return total

    abundants = []
    abundants_sum = list(range(n))
    res = list(range(1, n))
    for num in range(1, n):

        if getDivisors(num) > num:
            abundants.append(num)
        #print("%d/%d" % (num, n))
    for i, num in enumerate(abundants):
        for num2 in abundants[i:]:
            c = num + num2
            if c < n:
                abundants_sum[c] = 0
        #print("%d/%d" % (i, n))
    print(sum(abundants_sum))


def solve67():
    f = open("sources/problem67.txt", "r")
    lines = f.readlines()
    f.close()
    mem = [[] for i in range(len(lines))]
    i = 0
    for line in lines:
        try:
            mem[i] = line.strip().split(" ")
            mem[i] = list(map(int, mem[i]))
        except:
            pass
        i += 1
    for i in range(len(mem) - 2, -1, -1):
        for j in range(len(mem[i])):
            mem[i][j] = max(mem[i + 1][j], mem[i + 1][j + 1]) + mem[i][j]
    print(mem[0][0])
