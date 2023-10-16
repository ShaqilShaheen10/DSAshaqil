Sum of Factorial of digits
Let us define A(n) for positive integer N as a sum of factorials of its digits. For example, A(154) = 1!+ 5! +4! = 145. Given a number 'X', you need to print
the minimum number L, such that A(L) = X. If no such L exists, then print -1.

Input Format
First-line contains 'T' - the number of test cases. Then each line contains an integer 'X'.

Constraints
1 <= T <= 542 1000 <= X <= 10^9

Output Format
Print the answer for each value 'X'.

Sample Input 0
1
40321

Sample Output 0
18

Explanation 0
A(18) = 1!+ 8! = 40321 and 18 is the smallest element for which A(18) is 40321. Note, that A(80) = A(81) is also 40321. Among them, 18 is the smallest number.

Sample Input 1
1
120

Sample Output 1
5

Python Code:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
factorials = [factorial(i) for i in range(10)]
def sum_of_factorials(n):
    factorial_sum = 0
    while n > 0:
        digit = n % 10
        factorial_sum += factorials[digit]
        n //= 10
    return factorial_sum
def find_minimum_number(X):
    for i in range(1, 10**6):
        if sum_of_factorials(i) == X:
            return i
    return -1
T = int(input().strip())
for _ in range(T):
    X = int(input().strip())
    result = find_minimum_number(X)
    print(result)
