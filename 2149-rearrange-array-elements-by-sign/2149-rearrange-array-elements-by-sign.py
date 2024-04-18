class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v1 = []
        v2 = []
        v3 = []

        for num in nums:
            if num > 0:
                v1.append(num)
            else:
                v2.append(num)

        for i in range(len(v1)):
            v3.append(v1[i])
            v3.append(v2[i])

        return v3
                
        