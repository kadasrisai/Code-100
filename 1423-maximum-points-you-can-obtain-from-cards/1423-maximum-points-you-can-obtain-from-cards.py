class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        N, S = len(cardPoints), sum(cardPoints)
        wind = ans = sum(cardPoints[:N-k])

        for right in range(N-k,N):
            wind = wind - cardPoints[right - N + k] + cardPoints[right]
            ans = min(ans,wind)
        
        return S - ans
        