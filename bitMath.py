def bitMath(x: int, y: int, b: int) -> int:    
    if b & 1:
        return x
    elif not(b & 0):
        return y
    
def test_bitMath():
    assert bitMath(5, 9, 1) == 5
    assert bitMath(5, 9, 0) == 9