def count_ways(n, m):
    # Create a 2D matrix to store the number of ways to reach each cell
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Initialize the number of ways to reach the top-left corner to 1
    dp[0][0] = 1

    # Fill the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1]

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]

    # Fill the rest of the matrix
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # The number of ways to reach the bottom-right corner is stored in dp[n-1][m-1]
    return dp[n - 1][m - 1]

# Example usage
print(count_ways(2, 2))  # Output: 2
print(count_ways(5, 5))  # Output: 70