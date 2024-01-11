Convert 1d Array into 2D array
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array 
with m rows and n columns using all the elements from original.
The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) 
should form the second row of the constructed 2D array, and so on.
Print an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

Input Format
The first line have the N value
Second line having elements of array

Constraints
0 <= N <= 10^3

Output Format
Make 1d into 2d

Sample Input 0
4
1 2 3 4
2
2

Sample Output 0
1 2
3 4

Sample Input 1
3
1 2 3
1
3

Sample Output 1
1 2 3

Python Code:

def make_2d_array(original, m, n):
    if m * n != len(original):
        return []
    result = []
    for i in range(0, len(original), n):
        result.append(original[i:i + n])
    return result
N = int(input())
elements = list(map(int, input().split()))
m = int(input())
n = int(input())
result = make_2d_array(elements, m, n)
if not result:
    print("Empty 2D array")
else:
    for row in result:
        print(*row)
