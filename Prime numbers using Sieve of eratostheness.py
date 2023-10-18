Prime numbers using Sieve of eratostheness
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20, the output should be “2, 3, 5, 7, 11, 13, 17, 19”.

Input Format
Integer N

Constraints
no

Output Format
Print all primes smaller than or equal to n.

Sample Input 0
30

Sample Output 0
2 3 5 7 11 13 17 19 23 29

Sample Input 1
5

Sample Output 1
2 3 5

Python Code:

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    prime_numbers = [i for i in range(2, n + 1) if primes[i]]
    return prime_numbers
n = int(input())
prime_numbers = sieve_of_eratosthenes(n)
print(" ".join(map(str, prime_numbers)))
