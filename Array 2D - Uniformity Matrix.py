Array 2D - Uniformity Matrix
Rohit likes to play with numbers. He started to frame a matrix called uniformity matrix where he will be using either completely odd numbers or completely even
numbers but not both. Write a program to check whether he has framed the matrix in the correct order or not.

Input Format
The input consists of (n*n+1) integers.
The first integer corresponds to the number of rows/columns in the matrix.
The remaining integers correspond to the elements in the matrix.
The elements are read in row-wise order, the first row first, then the second row, and so on.

Output Format
Print Yes if it is a uniformity matrix.
Print No if it is not a uniformity matrix.

Sample Input 0
2
4 5
5 4
  
Sample Output 0
No
  
Sample Input 1
3
2 4 6
8 10 12
14 16 18
  
Sample Output 1
Yes
  
Python code:

def is_uniformity_matrix(matrix):
    n = matrix[0]
    odd_count = even_count = 0
    for i in range(1, n * n + 1):
        if matrix[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count == 0 or even_count == 0
n = int(input())
elements = []
for _ in range(n):
    elements.extend(list(map(int, input().split())))
if is_uniformity_matrix([n] + elements):
    print("Yes")
else:
    print("No")
