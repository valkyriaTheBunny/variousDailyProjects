from typing import Optional

def nearest(nums: list[int], index: int) -> Optional[int]:
    num = nums[index]
    closestDist = float('inf')
    closetNum = float('-inf')
    closestIndx = None

    for k, v in enumerate(nums):
        if k != index and abs(k - index) < closestDist and v > closetNum and v >  num:
            closestDist = abs(k - index)
            closetNum = v
            closestIndx = k

    return closestIndx

def nearestPreproc(nums: list[int]) -> list[Optional[int]]:
    n = len(nums)
    left = [None] * n
    right = [None] * n

    lStack = []
    for i in range(n):
        while lStack and nums[lStack[-1]] <= nums[i]:
            lStack.pop()
        if lStack:
            left[i] = lStack[-1]
        lStack.append(i)

    rStack = []
    for i in range(n - 1, -1, -1):
        while rStack and nums[rStack[-1]] <= nums[i]:
            rStack.pop()
        if rStack:
            right[i] = rStack[-1]
        rStack.append(i)

    nearest = [None] * n
    for i in range(n):
        l, r = left[i], right[i]
        if l is not None and r is not None:
            if abs(l - i) <= abs(r - i):
                nearest[i] = l
            else:
                nearest[i] = r
        elif l is not None:
            nearest[i] = l
        elif r is not None:
            nearest[i] = r

    return nearest

def test_nearest():
    assert nearest([4, 1, 3, 5, 6], 0) == 3

def test_nearestPreproc():
    nums = [4, 1, 3, 5, 6]
    lookup = nearestPreproc(nums)
    assert lookup[0] == 3
