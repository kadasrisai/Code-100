class Solution(object):
    
    def __init__(self):
        self.ans = []
        self.col = [False] * 10
        self.diag1 = [False] * 20
        self.diag2 = [False] * 20

    def dfs(self, cur, n):
        if len(cur) == n:
            self.ans.append(cur[:])
            return
        
        i = len(cur)
        cur.append("." * n)
        
        for j in range(n):
            if not self.col[j] and not self.diag1[i - j + n - 1] and not self.diag2[i + j]:
                # Place the queen
                cur[i] = cur[i][:j] + 'Q' + cur[i][j+1:]
                self.col[j] = self.diag1[i - j + n - 1] = self.diag2[i + j] = True
                
                # Recur to place the next queen
                self.dfs(cur, n)
                
                # Backtrack and remove the queen
                cur[i] = cur[i][:j] + '.' + cur[i][j+1:]
                self.col[j] = self.diag1[i - j + n - 1] = self.diag2[i + j] = False
        
        cur.pop()
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self.col = [False] * 10
        self.diag1 = [False] * 20
        self.diag2 = [False] * 20
        self.dfs([], n)
        return self.ans

        