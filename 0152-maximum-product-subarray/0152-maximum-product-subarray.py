class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf')
        prod = 1

        # Forward traversal
        for num in nums:
            prod *= num
            maxi = max(prod, maxi)
            if prod == 0:
                prod = 1

        prod = 1

        # Backward traversal
        for num in reversed(nums):
            prod *= num
            maxi = max(prod, maxi)
            if prod == 0:
                prod = 1

        return maxi
        