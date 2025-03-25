from itertools import combinations as combos

def poss_sum(nums: list[int], k: int) -> bool:
    comboSums = []

    for i in range(1, len(nums) + 1):
        for _combo in combos(nums, i):
            comboSums.append(sum(_combo))

    return k in comboSums

def test_poss_sum():
    assert poss_sum([20, 303, 3, 4, 25], 49) == True
