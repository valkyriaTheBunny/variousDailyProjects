def maxLength(nums: list[int]) -> int:
    nums.sort()
    seqLengths = []

    cnt = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            cnt += 1
        else:
            seqLengths.append(cnt)
            cnt = 1
    return max(seqLengths)

def test_maxLength():
    assert maxLength([5, 2, 99, 3, 4, 1, 100]) == 5
