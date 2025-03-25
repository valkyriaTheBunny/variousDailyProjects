def find_smallest_missing_positive(nums):
    smallest_missing = 1

    for num in nums:
        if num > smallest_missing:
            break
        smallest_missing += num 
    return smallest_missing

def test():
    arr = [1, 2, 3, 10]
    assert find_smallest_missing_positive(arr) == 7
