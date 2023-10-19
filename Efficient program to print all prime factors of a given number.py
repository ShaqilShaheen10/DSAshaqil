Efficient program to print all prime factors of a given number
Given a number n, write an efficient function to print all prime factors of n. For example, if the input number is 12, then the output should be “2 2 3”. And if 
the input number is 315, then the output should be “3 3 5 7”.

Input Format
Integer N

Constraints
No

Output Format
Prime factors of that integer

Sample Input 0
12

Sample Output 0
2 2 3

Sample Input 1
315

Sample Output 1
3 3 5 7

Python Code:

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
n = int(input())
factors = prime_factors(n)
print(' '.join(map(str, factors)))
