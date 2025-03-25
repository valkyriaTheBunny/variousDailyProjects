def partition(lst: list[any], pivot: int) -> list[any]:
    if pivot < min(lst) or pivot > max(lst):
        return lst

    lesser  = []
    equal = []
    greater = []

    for ele in lst:
        if ele > pivot:
            greater.append(ele)
        elif ele == pivot:
            equal.append(ele)
        else:
            lesser.append(ele)

    return lesser + equal + greater

def test_partition():
    assert partition([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]
