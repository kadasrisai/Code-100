class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return res