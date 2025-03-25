def square_then_sort(original: list[int]) -> list[int]:
    _original = original.copy()
    new_list = list(map(square, _original))
    new_list.sort()
    return new_list

def square(num: int) -> int:
    new_num = num ** 2
    return new_num

def test_square():
    assert square(4) == 16

def test_square_then_sort():
    assert square_then_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
