Set Matrix Zero(LeetCode)
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
Python Code
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M,N=len(matrix),len(matrix[0])
        firstrow,firstcol=False,False
        for r in range(M):
            if matrix[r][0]==0:
                firstcol=True
        for c in range(N):
            if matrix[0][c]==0:
                firstrow=True
        for r in range(M):
            for c in range(1,N):
                if matrix[r][c]==0:
                    matrix[r][0]=0
        for r in range(1,M):
            for c in range(1,N):
                if matrix[r][c]==0:
                    matrix[0][c]=0
        for r in range(1,M):
            if matrix[r][0]==0:
                matrix[r]=[0]*N
        for c in range(1,N):
            if matrix[0][c]==0:
                for i in range(1,M):
                    matrix[i][c]=0
        if firstrow:
            matrix[0]=[0]*N
        if firstcol:
            for i in range(M):
                matrix[i][0]=0
        return matrix
