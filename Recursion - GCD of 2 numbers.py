Recursion - GCD of 2 numbers
Write a program to compute the GCD of 2 numbers using recursion.

Input Format
Input consists of 2 integers.

Output Format
Output consists of one integer that represents the GCD of two numbers.

Sample Input 0
36
27

Sample Output 0
9

Sample Input 1
4
6

Sample Output 1
2

Python Code:

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
num1 = int(input())
num2 = int(input())
gcd = gcd_recursive(num1, num2)
print(gcd)
