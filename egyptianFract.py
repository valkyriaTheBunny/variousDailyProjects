def egyptian_fraction(a, b):
    fractions = []

    while a != 0:
        n = (b + a - 1) // a
        fractions.append(n)
        a = a * n - b
        b = b * n

    return fractions

result = egyptian_fraction(4, 13)
print("Egyptian Fraction Representation:", result)
