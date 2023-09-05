Rotate Array 29
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

Input Format
The first line have the M value
Second line have N value
Third-line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith rows constitutes column values separated by a single space

Output Format
90 degree Rotated Matrix in single line.

Sample Input 0
3
3
1 2 3
4 5 6
7 8 9

Sample Output 0
7 4 1 8 5 2 9 6 3

Sample Input 1
3
3
1 12 3
4 15 6
7 18 9

Sample Output 1
7 4 1 18 15 12 9 6 3

Python Code:

def rotate_matrix(matrix):
    n = len(matrix)
    rotated_matrix = []
    for i in range(n):
        rotated_row = []
        for j in range(n - 1, -1, -1):
            rotated_row.append(matrix[j][i])
        rotated_matrix.append(rotated_row)
    return rotated_matrix
M = int(input())
N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(*row, end=" ")
