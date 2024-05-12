class Solution(object):
    def nextPermutation(self, nums):
        # Step 1: Find the breaking point
        ind1 = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind1 = i
                break

        # If there is no breaking point
        if ind1 == -1:
            nums.reverse()
        else:
            # Step 2: Find next greater element and swap with ind2
            ind2 = -1
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[ind1]:
                    ind2 = i
                    break

            nums[ind1], nums[ind2] = nums[ind2], nums[ind1]

            # Step 3: Reverse the rest right half
            self.reverse(nums, ind1+1)

    def reverse(self, nums, start):
        i, j = start, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1