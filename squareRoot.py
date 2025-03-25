def squareRoot(num: int) -> float:
    if num <= 0:
        raise ValueError
    if num < 2:
        return num

    for i in range(2, int(num ** (1/2)) + 1):
        if i ** 2 == num:
            return num

    raise ValueError('Not a square number')
