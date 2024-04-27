class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i=0
        n=len(matrix)
        while i<n/2+1:
            #iterate over a square's sides in clockwise direction
            for j in range(i,n-i-1):
                t=matrix[i][j]
                r=matrix[j][n-i-1]
                b=matrix[n-i-1][n-j-1]
                l=matrix[n-j-1][i]
                #swap elements, placed at the same position on adjacent sides
                matrix[i][j]=l
                matrix[j][n-i-1]=t
                matrix[n-i-1][n-j-1]=r
                matrix[n-j-1][i]=b
            i+=1
        