class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis=[s[0]]
        for i in range(1,len(s)):
            if len(lis)==0 or lis[len(lis)-1]!=s[i]:
                lis.append(s[i])
            else:
                lis=lis[:len(lis)-1]        
        s="".join(lis)
        return s    
        