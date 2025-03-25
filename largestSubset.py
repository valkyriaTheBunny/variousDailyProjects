def largest_divisible_subset(nums):
    nums.sort()

    n = len(nums)
    dp = [1] * n
    parent = [-1] * n

    max_size = 0
    max_index = -1

    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        if dp[i] > max_size:
            max_size = dp[i]
            max_index = i

    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = parent[max_index]

    return result[::-1]

print(largest_divisible_subset([3, 5, 10, 20, 21]))
print(largest_divisible_subset([1, 3, 6, 24]))
