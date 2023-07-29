Arrays 2D - Transpose Matrix
Sheldon Cooper has a square-shaped puzzle made up of small square pieces containing numbers on them. He wants to rearrange the puzzle by changing the 
elements of a row into a column element and the column element into a row element without altering the shape of the puzzle. Help Sheldon solves this puzzle. 
Write a program to find the transpose of the given 2D matrix.

Input Format
The first line consists of an integer which represents the number of rows and columns. The next line consists of the elements in the matrix.

Output Format
Output prints the transpose of the input matrix.

Sample Input 0
3
1 2 3
4 5 6
7 8 9

Sample Output 0
1 2 3
4 5 6
7 8 9
Transpose matrix is:
1 4 7
2 5 8
3 6 9

Sample Input 1
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Sample Output 1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Transpose matrix is:
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16

Python Code:

def transpose_matrix(matrix, rows, cols):
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    return transpose
rows_cols = int(input())
rows = cols = rows_cols
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
transpose_matrix = transpose_matrix(matrix, rows, cols)
for row in matrix:
    print(" ".join(str(num) for num in row))
print("Transpose matrix is:")
for row in transpose_matrix:
    print(" ".join(str(num) for num in row))
