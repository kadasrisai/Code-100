class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub=float('-inf')
        pref_sum=0
        for num in nums:
            pref_sum+=num
            maxsub=max(maxsub,pref_sum)
            if pref_sum<0:
                pref_sum=0
            
        return maxsub
            
            
        
        