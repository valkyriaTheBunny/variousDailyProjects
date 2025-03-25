from itertools import combinations as combos

def max_XOR_Val(nums: list[int]) -> int:
    max = float('-inf')
    maxCombo = (0, 0)

    for combo in combos(nums, 2):
        xor_Val = combo[0] ^ combo[1]

        if xor_Val > max:
            max = xor_Val
            maxCombo = combo

    return (max, maxCombo)

print(max_XOR_Val([1, 2, 3, 4, 5, 7, 9]))
