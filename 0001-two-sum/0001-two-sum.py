class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        D = {}
        D[nums[0]] = 0
        for n in range(1, len(nums)):
            diff = target - nums[n]
            if diff in D:
                return [D[diff], n]
            else:
                D[nums[n]] = n
        