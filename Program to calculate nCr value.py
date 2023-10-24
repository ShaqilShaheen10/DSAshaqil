Program to calculate nCr value
Write a program to calculate the value of nCr.

Input Format
First Integer N
Second Integer R

Output Format
Value of nCr

Sample Input 0
5
2

Sample Output 0
10

Sample Input 1
3
1

Sample Output 1
3

Python Code:

n = int(input())
r = int(input())
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
nCr = factorial(n) // (factorial(r) * factorial(n - r))
print(nCr)
