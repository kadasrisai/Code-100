class Solution(object):
    def combinationSum(self, candidates, target):
        self.ans = []  # 2-D list to store the answer

        
        def solve(arr, i, current_sum, op):
            # If i crosses the array size, return
            if i >= len(arr):
                return

            if arr[i] + current_sum == self.target:
                op.append(arr[i])
                self.ans.append(op[:])
                op.pop()  # Backtrack
                return

            # If value at ith index + sum is less than target, include/exclude it in the combination
            if arr[i] + current_sum < self.target:
                # Include the current element
                op.append(arr[i])
                solve(arr, i, current_sum + arr[i], op)
                op.pop()  # Backtrack

            # Exclude the current element
            solve(arr, i + 1, current_sum, op[:])

        self.target = target
        op = []
        candidates.sort()  # Sort the array in ascending order
        solve(candidates, 0, 0, op)

        return self.ans
        