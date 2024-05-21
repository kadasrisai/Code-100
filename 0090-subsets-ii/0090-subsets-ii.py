class Solution(object):
    def subs(self, nums, res, sub, idx):
        # Add the current subset to the result
        res.append(sub[:])
        l = len(nums)
        
        for i in range(idx, l):
            # Skip duplicates
            if i != idx and nums[i] == nums[i - 1]:
                continue
            # Include the current element in the subset
            sub.append(nums[i])
            # Recurse with the next index
            self.subs(nums, res, sub, i + 1)
            # Backtrack: remove the current element before moving to the next iteration
            sub.pop()
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sub = []
        nums.sort()  # Sort the array to handle duplicates
        self.subs(nums, res, sub, 0)
        return res
    