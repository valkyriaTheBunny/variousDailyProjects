from collections import deque

def getMaxVals(nums: list[int], k: int) -> None:
    if not nums or k <= 0:
        return

    deq = deque()

    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            print(nums[deq[0]])

getMaxVals([10, 5, 2, 7, 8, 7], 3)
