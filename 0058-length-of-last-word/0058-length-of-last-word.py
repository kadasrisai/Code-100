class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=s.split()
        n=len(temp)
        return len(temp[n-1])