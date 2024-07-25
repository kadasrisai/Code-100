class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1] * len(nums)
        return self.solve(len(nums) - 1, nums, dp)

    def solve(self, n, nums, dp):
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        take = nums[n] + self.solve(n - 2, nums, dp)
        not_take = self.solve(n - 1, nums, dp)
        dp[n] = max(take, not_take)
        return dp[n]
        