ColumnWise Sum
Given a 2D integer array of size M*N, find and print the sum of ith column elements separated by space.

Input Format
The first line have the M value
Second line have N value
Third-line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith rows constitutes column values separated by a single space

Output Format
Sum of every ith column elements (separated by space)

Sample Input 0
4
2
1 2
3 4
5 6
7 8

Sample Output 0
16 20

Sample Input 1
1
1
17986 

Sample Output 1
17986

Python Code:

def sum_of_columns(arr, m, n):
    for j in range(n):
        column_sum = 0
        for i in range(m):
            column_sum += arr[i][j]
        print(column_sum, end=" ")
M = int(input())
N = int(input())
arr = []
for i in range(M):
    row = list(map(int, input().split()))
    arr.append(row)
sum_of_columns(arr, M, N)
