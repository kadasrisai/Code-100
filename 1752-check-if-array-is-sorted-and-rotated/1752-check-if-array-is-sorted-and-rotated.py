class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1,-1,-1):
            if i==0:
                return 1
            if nums[i]<nums[i-1]:
                break
        for j in range(i):
            if nums[j]>nums[j+1]:
                break
        if i-j==0 or i-j==1 and nums[-1] <= nums[0]:
            return 1
        else:
            return 0