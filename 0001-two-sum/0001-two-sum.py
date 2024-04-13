class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        d[nums[0]]=0
        for i in range(1,len(nums)):
            diff=target-nums[i]
            if diff in d:
                return [d[diff],i]
            else:
                d[nums[i]]=i
            