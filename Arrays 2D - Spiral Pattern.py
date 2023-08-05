Arrays 2D - Spiral Pattern
Given an integer matrix of size n*n. n is the number of rows and columns. Traverse it in a spiral form.

Input Format
The first line contains N, which represents the number of rows and columns of a matrix.
The next N lines contain N values, each representing the values of the matrix.

Output Format
A single line containing integers with space represents the desired traversal.

Sample Input 0
3 
1 2 3
4 5 6
7 8 9

Sample Output 0
1 2 3 6 9 8 7 4 5

Sample Input 1
4 
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Sample Output 1
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Python Code:

def spiral_traversal(matrix, n):
    top, bottom, left, right = 0, n - 1, 0, n - 1
    result = []
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
result = spiral_traversal(matrix, n)
print(' '.join(map(str, result)))
