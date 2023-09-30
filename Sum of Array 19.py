Sum of Array 19
Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.
  
Input Format
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Constraints
1 <= N <= 10^3

Output Format
sum

Sample Input 0
3
9 8 9

Sample Output 0
26

Sample Input 1
3
0 0 0

Sample Output 1
0

Python Code:

def sum_of_elements(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_of_elements(arr, n - 1)
n = int(input())
arr = list(map(int, input().split()))
print(sum_of_elements(arr, n))
