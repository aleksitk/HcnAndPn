from math import log

MAXN = 10 ** 18


# Generates a list of the first primes (with product > MAXN).
def gen_primes():
    primes = []
    primes_product = 1
    for n in range(2, 10 ** 10):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime:
            primes.append(n)
            primes_product *= n
            if primes_product > MAXN: break
    return primes


primes = gen_primes()


# Generates a list of the hcn <= MAXN.
def gen_hcn():
    # List of (number, number of divisors, exponents of the factorization)
    hcn = [(1, 1, [])]
    for i in range(len(primes)):
        new_hcn = []
        for el in hcn:
            new_hcn.append(el)
            if len(el[2]) < i: continue
            e_max = el[2][i - 1] if i >= 1 else int(log(MAXN, 2))
            n = el[0]
            for e in range(1, e_max + 1):
                n *= primes[i]
                if n > MAXN: break
                div = el[1] * (e + 1)
                exponents = el[2] + [e]
                new_hcn.append((n, div, exponents))
        new_hcn.sort()
        hcn = [(1, 1, [])]
        for el in new_hcn:
            if el[1] > hcn[-1][1]: hcn.append(el)
    return hcn


hcn = gen_hcn()


# From here on is only pretty printing.
# print("Number of highly composite numbers less than", MAXN, "is", len(hcn), "\n")


def PrintWithCorrectSpaces(a, b, c):
    aspace = int(log(MAXN, 10)) + 5
    bspace = int(log(hcn[-1][1], 10)) + 5
    assert (len(a) < aspace)
    assert (len(b) < bspace)

    print(a, " " * (aspace - len(a)), b, " " * (bspace - len(b)), c)


# PrintWithCorrectSpaces("number", "divisors", "factorization")


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def find_prime(x):
    i = 1
    if x == 1:
        return 1
    if x == 2:
        return 2
    x -= 1
    while not is_prime(x):
        i += 2
        if x - 2 > 0:
            x -= 2
        else:
            break
    return i


for i in range(len(hcn)):
    print(str(hcn[i][0]) + '             ' + str(find_prime(hcn[i][0])))
