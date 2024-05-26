class Solution(object):
    def __init__(self):
        self.ans = []
        self.sum = 0

    def dfs(self, cur, k, n, idx):
        if len(cur) == k and self.sum == n:
            self.ans.append(cur[:])  # Use cur[:] to create a copy of cur
            return
        elif len(cur) == k and self.sum > n:
            return
        
        for i in range(idx, 10):
            cur.append(i)
            self.sum += i
            self.dfs(cur, k, n, i + 1)
            cur.pop()
            self.sum -= i
    def combinationSum3(self, k, n):
        self.ans = []  # Initialize the answer list
        self.sum = 0   # Initialize the sum
        self.dfs([], k, n, 1)  # Start DFS with an empty current combination list
        return self.ans
        
        
        