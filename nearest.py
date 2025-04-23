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

def test_nearest():
    assert nearest([4, 1, 3, 5, 6], 0) == 3
