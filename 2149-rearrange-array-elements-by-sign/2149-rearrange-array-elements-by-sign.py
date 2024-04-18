class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        positive_index, negative_index = 0, 1

        for num in nums:
            if num > 0:
                ans[positive_index] = num
                positive_index += 2
            if num < 0:
                ans[negative_index] = num
                negative_index += 2

        return ans