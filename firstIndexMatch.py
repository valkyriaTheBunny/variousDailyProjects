from typing import Optional
def findMatch(nums: list[int]) -> Optional[int]:
    for i, num in enumerate(nums):
        if i == num:
            return num
    return None

def test_match():
    assert findMatch([-5, -3, 2, 3]) == 2
