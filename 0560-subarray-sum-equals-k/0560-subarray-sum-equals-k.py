class Solution(object):
    def subarraySum(self, nums, k):
        result = 0 
        prefix_sum = 0
        d = {0 : 1}
        
        for num in nums:
            prefix_sum = prefix_sum + num
            
            if prefix_sum - k in d:
                result = result + d[prefix_sum - k]
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1
                
        return result