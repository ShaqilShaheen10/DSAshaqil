Arrays 2D - Maximum element in each column
In a family, the people are arranged in rows and columns. Male persons in the families are arranged in a row and females are arranged in a column.
Find the eldest woman in each column. Write a program to find the maximum element in each column of the matrix.

Input Format
The input consists of (m*n+2) integers. The first integer corresponds to m, the number of rows in the matrix, and the second integer corresponds to n, 
the number of columns in the matrix. The remaining integers correspond to the elements in the matrix.The elements are read in row-wise order, the first row first,
then the second row, and so on.

Sample Input 0
3
2
4 5
6 9
0 3

Sample Output 0
6
9

Explanation 0
Here the maximum element in each column is 6 and 9 respectively and hence it prints, 6 9

Sample Input 1
3
3
22 23 25
25 22 26
26 27 23

Sample Output 1
26
27
26

Explanation 1
Here the maximum element in each column is 26,27 and 26 respectively and hence it prints, 26 27 26

Python Code:

def find_maximum_in_each_column(matrix, rows, cols):
    max_in_columns = []
    for j in range(cols):
        max_in_col = matrix[0][j]
        for i in range(1, rows):
            if matrix[i][j] > max_in_col:
                max_in_col = matrix[i][j]
        max_in_columns.append(max_in_col)
    return max_in_columns
def main():
    m = int(input()) 
    n = int(input()) 
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    max_in_columns = find_maximum_in_each_column(matrix, m, n)
    for max_value in max_in_columns:
        print(max_value)
if __name__ == "__main__":
    main()
