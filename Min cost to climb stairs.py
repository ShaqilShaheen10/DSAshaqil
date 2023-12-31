Min cost to climb stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
  
Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
  
Constraints
2 <= cost.length <= 1000
0 <= cost[i] <= 999
  
Output Format
Integer representing min cost

Sample Input 0
3
10 15 20

Sample Output 0
15

Explanation 0
You will start at index 1.
Pay 15 and climb two steps to reach the top.
The total cost is 15.

Sample Input 1
10
1 100 1 1 1 100 1 1 100 1

Sample Output 1
6

Explanation 1
You will start at index 0.
Pay 1 and climb two steps to reach index 2.
Pay 1 and climb two steps to reach index 4.
Pay 1 and climb two steps to reach index 6.
Pay 1 and climb one step to reach index 7.
Pay 1 and climb two steps to reach index 9.
Pay 1 and climb one step to reach the top.
The total cost is 6.

Python Code:

def min_cost_to_climb_stairs(n, cost):
    if n == 2:
        return min(cost[0], cost[1])
    min_cost = [0] * n
    min_cost[0] = cost[0]
    min_cost[1] = cost[1]
    for i in range(2, n):
        min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
    return min(min_cost[n - 1], min_cost[n - 2])
n = int(input().strip())
cost = list(map(int, input().strip().split()))
result = min_cost_to_climb_stairs(n, cost)
print(result)
