def seive(num: int) -> list[int]:
    prime = [True for i in range(num + 1)]
    p = 2

    while (p * p <= num):
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False

        p += 1

    intPrimes = []
    for p in range(2, num + 1):
        if prime[p]:
            intPrimes.append(p)

    return intPrimes

print(seive(100))
