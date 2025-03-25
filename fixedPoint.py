def findFixedPoint(arr: list[int]) -> int | bool:
    for index, num in enumerate(arr):
        if num == index:
            return num
    return False

def test_findFixedPoint():
    assert findFixedPoint([-6, 0, 2, 40]) == 2

def test_noFixedPoint():
    assert findFixedPoint([1, 5, 7, 8]) == False
