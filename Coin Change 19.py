Coin Change 19
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
Third line contains an integer 'X'.
  
Constraints
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
  
Output Format
Integer representing fewer number of coins
  
Sample Input 0
3
1 2 5
11
  
Sample Output 0
3
  
Explanation 0
11 = 5 + 5 + 1

Sample Input 1
1
2
3

Sample Output 1
-1

Python Code:

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
N = int(input())
coins = list(map(int, input().split()))
X = int(input())
result = min_coins(coins, X)
print(result)
