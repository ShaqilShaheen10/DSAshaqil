Power of 2
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.
Do this by bit manipultion

Input Format
Integer N

Constraints
-2^31 <= n <= 2^31 - 1

Output Format
true or false

Sample Input 0
3

Sample Output 0
false

Sample Input 1
2

Sample Output 1
true

Python Code:

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
n0 = int(input())
print(str(is_power_of_two(n0)).lower())
