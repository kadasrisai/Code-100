class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev=0
        if(x<0):
            return False
        while temp!=0:
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
        if rev==x:
            return True
        else:
            return False
        