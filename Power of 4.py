Power of 4
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.

Input Format
Take a number input

Constraints
-2^31 <= n <= 2^31 - 1

Output Format
true or false

Sample Input 0
13

Sample Output 0
false

Sample Input 1
4

Sample Output 1
true

Python Code:

def is_power_of_four(n):
    if n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0:
        return "true" 
    else:
        return "false"
n = int(input())
print(is_power_of_four(n))
