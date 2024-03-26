class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zero_count=[]
        one_count=[]
        two_count=[]
        for i in range(n-1,-1,-1):
            if nums[i]==0:
                zero_count.append(0)
                nums.pop(i)
            elif nums[i]==1:
                one_count.append(1)
                nums.pop(i)
            elif nums[i]==2:
                two_count.append(2)
                nums.pop(i)
        nums.extend(zero_count)
        nums.extend(one_count)
        nums.extend(two_count)
        print(nums)
