Arrays 2D - Matrix Rotation
Mr. Bean has saved an image in a 2D array and he wants to rotate the image by 90 degrees in clockwise direction. Please help him code for array rotation
by 90 degrees in clockwise direction.

Input Format
The first line contains the size of the matrix N. The next N lines contain the elements of the matrix

Output Format

The output prints the rotated matrix

Sample Input 0
3
1 2 3
4 5 6
7 8 9

Sample Output 0
7 4 1
8 5 2
9 6 3

Explanation 0
The output is the 90-degree clockwise rotated matrix. Try to visualize.

Sample Input 1
3
-5 -10 -4 
3 -6 3 
-1 0 -6 

Sample Output 1
-1 3 -5
0 -6 -10
-6 3 -4

Explanation 1
The output is the 90-degree clockwise rotated matrix. Try to visualize.

Python Code:

def rotate_matrix_clockwise(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
rotated_matrix = rotate_matrix_clockwise(matrix)
for row in rotated_matrix:
    print(*row)
