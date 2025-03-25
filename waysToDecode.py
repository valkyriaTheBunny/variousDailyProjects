def count_decodings(message):
    n = len(message)
    
    # Create an array to store the count of decodings
    dp = [0] * (n + 1)
    
    # Empty string can be decoded in 1 way
    dp[0] = 1
    
    # Single digit can be decoded in 1 way if not '0'
    dp[1] = 1 if message[0] != '0' else 0
    
    for i in range(2, n + 1):
        # Check if the single digit is not '0'
        if message[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Check if the two digits form a valid mapping (between 10 and 26)
        two_digit = int(message[i - 2 : i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]

# Example usage:
encoded_message = "111"
result = count_decodings(encoded_message)
print(result)
