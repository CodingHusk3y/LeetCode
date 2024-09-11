class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Dynamic Programming approach
        m, n = len(text1), len(text2)
        
        # Initialize a DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table using a bottom-up approach
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The result is stored in the bottom-right cell of the DP table
        return dp[m][n]