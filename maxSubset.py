from itertools import combinations as combo

def maxSubsetSum(nums: list[int]) -> int:
    comboSums = []

    for i in range(1, len(nums) + 1):
        for _combo in combo(nums, i):
            comboSums.append(sum(_combo))

    return max(comboSums)

def test_maxSubsetSum():
    assert maxSubsetSum([8, -1, 3, 4]) == 15
    assert maxSubsetSum([-4, 5, 1, 0]) == 6

if __name__ == "__main__":
    print(maxSubsetSum([8, -1, 3, 4]))
