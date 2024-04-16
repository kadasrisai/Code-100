class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen, ans = [True] * n, 0
        p=2
        while (p*p<=n):
            if seen[p]:
                for i in range(p*p,n,p):
                    seen[i]=False    
            p+=1
        
        for p in range(2, n):
            if seen[p]:
                ans+=1
        return ans
            
            