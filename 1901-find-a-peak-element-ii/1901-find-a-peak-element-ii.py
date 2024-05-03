class Solution(object):
    def findMax(self, mat, col):
        maxRow = 0
        for i in range(len(mat)):
            maxRow = i if mat[i][col] >= mat[maxRow][col] else maxRow
        return maxRow

    def predicate(self, midCol, mat, leftCol, rightCol):
        maxRow = self.findMax(mat, midCol)
        rejectRight = (midCol + 1 <= rightCol) and (mat[maxRow][midCol + 1] < mat[maxRow][midCol])
        return rejectRight
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        leftCol = 0
        rightCol = len(mat[0]) - 1
        while leftCol < rightCol:
            midCol = leftCol + (rightCol - leftCol) // 2
            if self.predicate(midCol, mat, leftCol, rightCol):
                rightCol = midCol
            else:
                leftCol = midCol + 1
                        
        maxRow = self.findMax(mat, leftCol)
        return [maxRow, leftCol]
        