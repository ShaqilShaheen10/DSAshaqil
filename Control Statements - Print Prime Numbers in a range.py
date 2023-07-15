Control Statements - Print Prime Numbers in a range
A prime number is divisible only by 1 and itself. You are given a positive integer. Write an algorithm to find all the prime numbers from 2 to the 
given positive number

Input Format
The input consists of an integer.

Constraints
1 < n< 109

Output Format
Print space-separated integers representing the prime numbers till the given positive number.

Sample Input 0
11

Sample Output 0
2 3 5 7 11

Explanation 0
For the given number the list of special numbers is [2, 3, 5, 7, 11]

Sample Input 1
30

Sample Output 1
2 3 5 7 11 13 17 19 23 29

Explanation 1
For the given number the list of special numbers is [2,3, 5, 7, 11, 13, 17, 19, 23, 29]

Python Code:

def find_primes(n):
    primes=[]
    for num in range(2, n+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes
num=int(input())
prime_numbers=find_primes(num)
print(" ".join(map(str, prime_numbers)))
