class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=len(nums)//2
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
                if d[i]>temp:
                    return i
            else:
                d[i]=1
        return nums[0]
