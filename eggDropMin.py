def egg_drop(num_eggs: int, num_floors: int):
    dp = [[0] * (num_floors + 1) for _ in range(num_eggs + 1)]

    for i in range(1, num_eggs + 1):
        dp[i][0] = 0  # 0 floors
        dp[i][1] = 1  # 1 floor

    for j in range(1, num_floors + 1):
        dp[1][j] = j

    for n in range(2, num_eggs + 1):
        for m in range(2, num_floors + 1):
            dp[n][m] = float('inf')
            low, high = 1, m
            while low <= high:
                mid = (low + high) // 2
                break_case = dp[n-1][mid-1]
                not_break_case = dp[n][m-mid]

                worst_case = 1 + max(break_case, not_break_case)

                if break_case > not_break_case:
                    high = mid - 1
                else:
                    low = mid + 1

                dp[n][m] = min(dp[n][m], worst_case)

    return dp[num_eggs][num_floors]

def test_egg_drop():
    assert egg_drop(2, 10) == 4
