House robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into 
on the same night. Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight
without alerting the police.

Input Format
The first line consists of size of an array The second line consists of array of elements separated by space

Constraints
1<=n<=10 1<=Ai<=10000

Output Format
The output consists of maximum amount stolen

Sample Input 0
4
11 12 13 11

Sample Output 0
24

Explanation 0
Rob house 1 (money = 11) and then rob house 3 (money = 13). Total amount you can rob = 11 + 13 = 24.

Sample Input 1
4
4 3 2 11

Sample Output 1
15

Python Code:

def rob_houses(n, nums):
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[n - 1]
n = int(input())
nums = list(map(int, input().split()))
print(rob_houses(n, nums))
