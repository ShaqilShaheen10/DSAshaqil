Control Statements - Strong Number

A number can be said as a strong number when the sum of the factorial of the individual digits is equal to the number.
For example, 145 is a strong number. 1! + 4! + 5! = 145. Write a program to check whether a given number is a strong number or not.

Input Format
Input consists of 1 integer.

Output Format
If it is a strong number print "Yes" or print "No".

Sample Input 0
145

Sample Output 0
Yes

Explanation 0
= 1! + 4! +5! = 1+24+120 = 145

Python Code:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def is_strong_number(num):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += factorial(digit)
        temp //= 10
    if digit_sum == num:
        return "Yes"
    else:
        return "No"
num = int(input())
result = is_strong_number(num)
print(result)
