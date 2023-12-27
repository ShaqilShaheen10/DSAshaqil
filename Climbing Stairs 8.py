Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input Format
Integer N

Constraints
1 <= n <= 45

Output Format
Number of ways in which we can climb stairs

Sample Input 0
2

Sample Output 0
2

Explanation 0
There are two ways to climb to the top.
1 step + 1 step
2 steps

Sample Input 1
3

Sample Output 1
3

Explanation 1
There are three ways to climb to the top.
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step

Python Code:

def climb_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
n0 = int(input())
print(climb_stairs(n0))
