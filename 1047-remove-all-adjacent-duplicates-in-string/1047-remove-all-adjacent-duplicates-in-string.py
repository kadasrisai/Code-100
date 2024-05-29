class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        
        return ''.join(stack)   
        