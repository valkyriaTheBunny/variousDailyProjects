from typing import Optional
def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True

def findPrimes(num: int) -> Optional[tuple[int, int]]:
    if num <= 2:
        return
    for i in range(2, num // 2 + 1):
        if isPrime(i) and isPrime(num - i):
            return (i, num - i)

def test_findPrimes():
    assert findPrimes(4) == (2, 2)
    assert findPrimes(10) == (3, 7)
