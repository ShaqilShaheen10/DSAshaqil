All Indices of Number
Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array.
Do this recursively. Indexing in the array starts from 0.

Input Format
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Constraints
1 <= N <= 10^3

Output Format
indexes where x is present in the array (separated by space)

Sample Input 0
5
9 8 10 8 8
8

Sample Output 0
1 3 4

Sample Input 1
5
9 8 10 8 8
9

Sample Output 1
0

Python Code:

def find_indexes(arr, x, index=0, result=[]):
    if index == len(arr):
        return result
    if arr[index] == x:
        result.append(index)
    return find_indexes(arr, x, index + 1, result)
N = int(input())
arr = list(map(int, input().split()))
x = int(input())
indexes = find_indexes(arr, x)
print(" ".join(map(str, indexes)))
