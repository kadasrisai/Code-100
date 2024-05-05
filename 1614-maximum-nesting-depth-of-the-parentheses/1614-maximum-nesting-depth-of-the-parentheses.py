class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        tmp = 0
        for c in s:
            if c == "(":
                tmp += 1
            elif c == ")":
                if tmp > output:
                    output = tmp
                tmp -= 1
        return output
        