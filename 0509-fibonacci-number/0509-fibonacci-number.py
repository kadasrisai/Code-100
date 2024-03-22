class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        sum=0
        count=0
        
        while count<n:
            count+=1
            a=b
            b=sum
            sum=a+b
        return sum
        