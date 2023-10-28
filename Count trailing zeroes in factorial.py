Count trailing zeroes in factorial
Given an integer n, write a function that returns count of trailing zeroes in n!.

Input Format
Integer N

Output Format
Trailing zeros in n!

Sample Input 0
5

Sample Output 0
1

Explanation 0
Factorial of 5 is 120 which has one trailing 0.

Sample Input 1
20

Sample Output 1
4

Explanation 1
Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.

Python Code:

def count_trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count
n = int(input())
print(count_trailing_zeros(n))
