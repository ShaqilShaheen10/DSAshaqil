Linear Search Recursively
Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.
  
Input Format
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
  
Constraints
1 <= N <= 10^3

Output Format
true or false

Sample Input 0
3
9 8 10
8
  
Sample Output 0
true
  
Sample Input 1
3
9 8 10
2
  
Sample Output 1
false

Python Code:

def is_present(arr, n, x):
    if n == 0:
        return "false"
    if arr[0] == x:
        return "true"
    return is_present(arr[1:], n - 1, x)
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = is_present(arr, n, x)
print(result)
