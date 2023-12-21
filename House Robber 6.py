House Robber 6
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
  
Constraints
1 <= nums.length <= 100
0 <= nums[i] <= 400
  
Output Format
Return the maximum amount of money you can rob tonight without alerting the police.
  
Sample Input 0
4
1 2 3 1

Sample Output 0
4

Explanation 0
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4

Sample Input 1
5
2 7 9 3 1

Sample Output 1
12

Explanation 1
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Python Code:

def rob_houses(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]
N = int(input())
nums = list(map(int, input().split()))
result = rob_houses(nums)
print(result)
