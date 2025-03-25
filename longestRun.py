def longestRun(num: int) -> int:
    binary = format(num, 'b')
    longestRun = -1
    currRun = 0

    for char in binary:
        if char == '1':
            currRun += 1
        else:
            if currRun > longestRun:
                longestRun = currRun
            currRun = 0

    return longestRun

def test_longestRun():
    assert longestRun(156) == 3
