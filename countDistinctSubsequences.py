# https://practice.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1
def countDistinctSubsequences(s):
    n = len(s)
    mod = 10**9 + 7
    
    # Initialize a list to store the count of distinct subsequences ending at each index
    dp = [0] * (n + 1)
    
    # Initialize dp[0] as 1 because there's always an empty subsequence
    dp[0] = 1
    
    # Create a dictionary to store the most recent occurrence of each character
    last_occurrence = {}
    
    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % mod
        
        if s[i - 1] in last_occurrence:
            dp[i] = (dp[i] - dp[last_occurrence[s[i - 1]] - 1] + mod) % mod
        
        last_occurrence[s[i - 1]] = i
    
    return dp[-1]

# Example usage
s = "abcb"
result = countDistinctSubsequences(s)
print("Number of distinct subsequences:", result)
