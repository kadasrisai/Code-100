class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 0
        intervals = sorted(intervals , key = lambda x : x[1])
        last_end = intervals[0][1]
        
        for interval in intervals[1:]:
            current_start = interval[0]
            current_end = interval[1]
            
            if current_start >= last_end:
                last_end = current_end
            else:
                result = result + 1
                
        return result
        