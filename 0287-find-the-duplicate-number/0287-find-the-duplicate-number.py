class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
                
        for i in dict:
            if dict[i] > 1:
                return i
            
        