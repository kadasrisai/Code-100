class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=0
        len1=0
        for i in range(len(nums)):
            if nums[i]==1:
                len1+=1
            else:
                max_len=max(len1,max_len)
                len1=0
        max_len=max(len1,max_len)   
        return max_len