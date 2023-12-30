Matrix chain Multiplication 9
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses
to minimize the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.

Input Format
The first line of input contains an integer, that denotes the value of n. The following line contains n+1 integers, that denote the value of elements of array p[].

Constraints
1 <= n <= 100
Time limit: 1 second

Output Format
The first and only line of output prints the minimum number of multiplication needed.

Sample Input 0
3
10 15 20 25

Sample Output 0
8000

Explanation 0
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000.

Sample Input 1
4
5 10 15 20 25

Sample Output 1
4750

Python Code:

def matrix_chain_multiplication(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]
n = int(input())
p = list(map(int, input().split()))
result = matrix_chain_multiplication(p)
print(result)
