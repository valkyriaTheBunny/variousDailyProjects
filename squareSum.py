squares = [1, 4, 9, 16, 25, 36, 49,
    64, 81, 100, 121, 144, 169, 196,
    225, 256, 289, 324, 361, 400, 441,
    484, 529, 576, 625, 676, 729, 784,
    841, 900, 961, 1024, 1089, 1156, 1225]

def sqrSum(num: int) -> int:
    if num <= 0:
        return 0
    if num in squares:
        return 1
    closet = float('inf')
    for sqr in squares:
        if num - sqr < closet:
            return  1 + sqrSum(num - sqr)

def test_sqrSum_square():
    assert sqrSum(4) == 1

def test_sqrSum():
    assert sqrSum(17) == 2
