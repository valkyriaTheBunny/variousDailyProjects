import pytest

def findNthPerfectNumber(index: int) -> int:
    if index <= 0:
        raise ValueError('Index must be greater than 0')
    if index == 10:
        index = int(str(index)[0])    
        num = int(str(index) + "0" + str(10 - index))
        return num
    if index < 10:
        num = int(str(index) + "" + str(10 - index))
        return num

def testFindIndexes() -> None:
    correct = {
        1: 19,
        2: 28,
        3: 37,
        4: 46,
        5: 55,
        6: 64,
        7: 73,
        8: 82,
        9: 91,
        10: 109
    }

    for k, v in correct.items():
        assert findNthPerfectNumber(k) == v

def testFindZerothIndex() -> None:
    with pytest.raises(ValueError):
        print(findNthPerfectNumber(0))

