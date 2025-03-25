def secLargeVal(nums: list[int]) -> int:
    maxN = float('-inf')
    secLargeN = float('-inf')

    for num in nums:
        if num <= maxN and num > secLargeN:
            secLargeN = num
        elif num > maxN:
            maxN = num

    return secLargeN

def test_secLargeVal():
    assert secLargeVal([10, 8, 13, 17, 9, 14, 100, 95, 45, 6]) == 95
