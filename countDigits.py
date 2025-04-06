def countDigits(num: int) -> int:
    return len(str(num))

def test_countDigits():
    assert countDigits(567) == 3
