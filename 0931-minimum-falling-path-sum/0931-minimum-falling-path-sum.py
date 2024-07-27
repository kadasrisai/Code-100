class Solution(object):
    def minFallingPathSum(self, matrix):
        # initialize dp
        dp = [[0] * len(matrix) for i in range(len(matrix))]
        
		# copy first row as it is in the dp
        for i in range(len(dp[0])):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, len(dp)):
            for j in range(len(dp)):
				# check the three(or available) values from the previous row
                l = dp[i - 1][j - 1] if j > 0 else float('inf')
                u = dp[i - 1][j]
                r = dp[i - 1][j + 1] if j < len(dp[i]) - 1 else float('inf')
				
				# make dp[i][j] the min of the values
                dp[i][j] = min(l, u, r) + matrix[i][j]
        
        return min(dp[-1])
        