class Solution(object):
    def reversePairs(self, nums):
        self.count = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.count

    def merge_sort(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        merged = []
        p1, p2 = start, mid + 1
        while p1 <= mid and p2 <= end:
            if nums[p1] > 2 * nums[p2]:
                self.count += mid - p1 + 1
                p2 += 1
            else:
                p1 += 1

        p1, p2 = start, mid + 1
        while p1 <= mid and p2 <= end:
            if nums[p1] <= nums[p2]:
                merged.append(nums[p1])
                p1 += 1
            else:
                merged.append(nums[p2])
                p2 += 1

        while p1 <= mid:
            merged.append(nums[p1])
            p1 += 1

        while p2 <= end:
            merged.append(nums[p2])
            p2 += 1

        for i in range(len(merged)):
            nums[start + i] = merged[i]