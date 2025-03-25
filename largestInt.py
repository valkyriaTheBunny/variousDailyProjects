from functools import cmp_to_key

def largestNum(nums: list[int]) -> int:
    str_nums = list(map(str, nums))

    def compare(x, y):
        if x + y > y + x:
            return -1
        else:
            return 1

    sorted_nums = sorted(str_nums, key=cmp_to_key(compare))

    largest_num = ''.join(sorted_nums)

    return int(largest_num) if largest_num[0] != '0' else 0

def test_largestInt():
    assert largestNum([10, 7, 76, 415]) == 77641510
