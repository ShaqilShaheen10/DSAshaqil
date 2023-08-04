Arrays 2D - Sum of rows and columns
Ram has a fruit shop. He has arranged some set of fruits in the column and row-wise. Ram needs to find which row and column have a maximum number of fruits. 
Help him to find out.

Input Format
Input consists of 2 integers(size of rows and columns) and 1 2D array.
  
Output Format
The output prints the sum of all rows and columns as well as print the row and column which has the maximum sum. Refer to the sample output.

Sample Input 0
3
3
1 6 8
2 5 1
3 8 2

Sample Output 0
The Sum of rows is 15 8 13
Row 1 has a maximum sum
The Sum of columns is 6 19 11
Column 2 has the maximum sum

Explanation 0
Here the sum of rows and columns is 15,18,13 and 6,9,11 respectively. Then it will compare the values and print the greatest sum(row and column).

Sample Input 1
2
2
5 7
9 7

Sample Output 1
The Sum of rows is 12 16
Row 2 has a maximum sum
The Sum of columns is 14 14
Column 1 has the maximum sum

Explanation 1
Here the sum of rows and columns is 12,16 and 14,14 respectively. Then it will compare the values and print the greatest sum(row and column).

Python Code:

def find_max_sum_indices(arr):
    max_sum_row = max_sum_col = float('-inf')
    max_sum_row_index = max_sum_col_index = -1
    rows_sum = [sum(row) for row in arr]
    cols_sum = [sum(col) for col in zip(*arr)]
    for i, row_sum in enumerate(rows_sum):
        if row_sum > max_sum_row:
            max_sum_row = row_sum
            max_sum_row_index = i + 1 
    for j, col_sum in enumerate(cols_sum):
        if col_sum > max_sum_col:
            max_sum_col = col_sum
            max_sum_col_index = j + 1
    return max_sum_row_index, max_sum_col_index
num_rows = int(input())
num_cols = int(input())
matrix = []
for _ in range(num_rows):
    row = list(map(int, input().split()))
    matrix.append(row)
max_sum_row_index, max_sum_col_index = find_max_sum_indices(matrix)
print("The Sum of rows is", " ".join(str(sum(row)) for row in matrix))
print("Row", max_sum_row_index, "has a maximum sum")
column_sums = [sum(col) for col in zip(*matrix)]
print("The Sum of columns is", " ".join(map(str, column_sums)))
print("Column", max_sum_col_index, "has the maximum sum")
