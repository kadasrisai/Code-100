class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def digi_sum(num):
            temp=num
            digisum=0
            while temp!=0:
                rem=temp%10
                digisum+=rem
                temp=temp//10
            if len(str(digisum))==1:
                return digisum
            else:
                return digi_sum(digisum)
        ans=digi_sum(num)
        return ans
        