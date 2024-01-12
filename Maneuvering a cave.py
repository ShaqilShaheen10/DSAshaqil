Maneuvering a cave
Maneuvering a cave
A robot wants to move through a cave of grid M x N from (M-1,N-1) to (M/2,N/2). It can only move up or left. Calculate the total number of ways the robot
can reach the destination.

Input Format
The two integer inputs represent the number of rows and columns.

Constraints
-10^5 to 10^5

Output Format
Integer value represents the number of ways to reach the destination

Sample Input 0
4
4

Sample Output 0
20

Sample Input 1
7
7

Sample Output 1
924

Python Code:

def count_ways_to_destination(M, N):
    dp = [[0] * N for _ in range(M)]
    for i in range(M):
        dp[i][0] = 1
    for j in range(N):
        dp[0][j] = 1
    for i in range(1, M):
        for j in range(1, N):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[M - 1][N - 1]
M0 = int(input())
N0 = int(input())
print(count_ways_to_destination(M0, N0))
