Control Statements - Sum of digit till single digit
Write a program to find the sum of digits of a number until the sum becomes a single digit.

Input Format
Input format consists of a number

Output Format
Output format consists of an integer

Sample Input 0
78945623

Sample Output 0
8

Sample Input 1
45678

Sample Output 1
3

Python Code:

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
num = int(input())
while num >= 10:
    num = sum_of_digits(num)
print(num)
