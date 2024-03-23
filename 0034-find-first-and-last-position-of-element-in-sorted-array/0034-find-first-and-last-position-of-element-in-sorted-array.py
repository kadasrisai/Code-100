class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums)
        left, right = -1, -1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        left = start
        
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        right = start
        
        return [-1, -1] if left == right else [left, right - 1]
        
        