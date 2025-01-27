import random


def find_factor(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return i
        i += 1
    return x


def is_even(x):
    return x % 2 == 0


def mult_three(x):
    if x < 10:
        return x in list(3, 6, 9)
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return mult_three(sum)


def exp(x, y):
    if y == 0:
        return 1
    if y % 2 == 1:
        return x * exp(x, y - 1)
    c = exp(x, y / 2)
    return c * c


def mod_exp(x, y, k):
    if k == 1:
        return 0
    if y == 0:
        return 1
    if y % 2 == 1:
        return (x * mod_exp(x, y - 1, k)) % k
    c = mod_exp(x, y / 2, k) % k
    return (c * c) % k


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def find_period(a, n):
    found = False
    L = []
    x = 1
    while not found:
        v = (a**x) % n
        x += 1
        if v in L:
            found = False
        else:
            L.append(v)
    return len(L)


def shor(n):
    # ignore 2, 3, 5
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5

    # Check if n is prime
    if gcd(n, 1) == 1 and n > 1:
        return n

    a = random.randint(1, n - 1)
    x = gcd(a, n)
    if x != 1:
        return x
    r = find_period(a, n)
    if r % 2 == 1:
        return None
    if pow(a, r // 2, n) == n - 1:
        return None
    e = pow(a, r // 2, n)
    test1 = gcd(e + 1, n)
    test2 = gcd(e - 1, n)
    if test1 != 1 and test1 != n:
        return test1
    elif test2 != 1 and test2 != n:
        return test2
    return None


def factor(n):
    fact = []
    while n > 1:
        res = shor(n)
        fact.append(res)
        n = n / res
    return fact


if __name__ == "__main__":
    print(factor(21))
