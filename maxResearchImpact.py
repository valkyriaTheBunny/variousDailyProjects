def calcResearchImpact(nums: list[int]) -> int:
    nums.sort(reverse=True)

    h_index = 0
    for i in range(len(nums)):
        if nums[i] >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index

def test_calcResearchImpact():
    assert calcResearchImpact([4, 3, 0, 1, 5]) == 3
