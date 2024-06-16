class Solution:
    def func(self, mid, k, v):
        n = len(v)
        sum_ = 0
        for i in range(mid):
            sum_ += v[i]
        if sum_ >= k:
            return True
        
        for i in range(mid, n):
            sum_ += v[i] - v[i - mid]
            if sum_ >= k:
                return True
        
        return False

    def minSubArrayLen(self, t, v):
        n = len(v)
        s = 0
        ans = s
        e = n
        while s <= e:
            mid = (s + e) // 2
            if self.func(mid, t, v):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans