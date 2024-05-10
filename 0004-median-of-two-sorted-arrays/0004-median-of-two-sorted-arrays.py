class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        
        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2
        left = (n1 + n2 + 1) // 2  # Calculate the left partition size
        low, high = 0, n1
        
        while low <= high:
            mid1 = (low + high) // 2  # Calculate mid index for nums1
            mid2 = left - mid1  # Calculate mid index for nums2
            
            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                low = mid1 + 1
        
        return 0