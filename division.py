import pytest

def divide(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError('0 not an accepted value')
    times = 0
    if b > a:
        return 0
    
    while a > 0:
        a -= b
        times += 1
    return times

def test_set_first_param_zero():
    with pytest.raises(ValueError):
        divide(0, 1)

def test_set_second_param_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide():
    result = 12 / 4
    assert divide(12, 4) == result
    result2 = 3 // 4
    assert divide(3, 4) == result2