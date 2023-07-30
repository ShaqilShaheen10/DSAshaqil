Arrays 2D - Matrix Multiplication
Write a program to multiply two matrices of the same dimensions together.

Input Format
The first two integer inputs, m, and n represent the dimensions of both of the matrices that have to be multiplied. Next (m*n) integers represent 
the elements in the first matrix and followed by another (m*n) integer representing the elements in the second matrix

Output Format
The output consists of (m*n) integers representing the values of the matrix that is the product of both the input matrices.

Sample Input 0
3 3
1 2 3
4 5 6
7 8 9
9 8 7
6 5 4
3 2 1

Sample Output 0
30 24 18
84 69 54
138 114 90

Sample Input 1
3 3
4 5 1 
9 8 5
2 5 8
1 2 3
4 5 6
7 8 9

Sample Output 1
31 41 51
76 98 120
78 93 108

Python Code:

def multiply_matrices(m, n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
def main():
    m, n = map(int, input().split())
    matrix1 = []
    matrix2 = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix1.append(row)
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix2.append(row)
    result = multiply_matrices(m, n, matrix1, matrix2)
    for row in result:
        print(" ".join(map(str, row)))
if __name__ == "__main__":
    main()
