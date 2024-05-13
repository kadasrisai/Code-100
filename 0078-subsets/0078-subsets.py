class Solution(object):
    def subsets(self, nums):
        subs = []
        sub = []
        self._subsets(nums, 0, sub, subs)
        return subs
    
    def _subsets(self, nums, i, sub, subs):
        subs.append(sub[:])
        for j in range(i, len(nums)):
            sub.append(nums[j])
            self._subsets(nums, j + 1, sub, subs)
            sub.pop()
        