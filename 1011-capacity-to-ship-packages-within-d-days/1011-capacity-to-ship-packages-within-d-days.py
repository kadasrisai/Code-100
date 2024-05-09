class Solution(object):
    def ispossible(self, weights, n, m, mid):
        daysCount = 1
        shipSum = 0
        for weight in weights:
            if weight > mid:
                return False
            if weight + shipSum > mid:
                daysCount += 1
                shipSum = weight
                if daysCount > m:
                    return False
            else:
                shipSum += weight
        return True
    
    
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        start = 0
        n = len(weights)
        end = sum(weights)
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.ispossible(weights, n, days, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
        