Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square.
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.
  
Input Format
First Line Array size
Second line elements of array
  
Constraints
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
  
Output Format
true or false
  
Sample Input 0
5
1 1 2 2 2
  
Sample Output 0
true
  
Explanation 0
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Sample Input 1
5
3 3 3 3 4
  
Sample Output 1
false
  
Explanation 1
Explanation: You cannot find a way to form a square with all the matchsticks.

Python Code:

def makesquare(matchsticks):
    total_length = sum(matchsticks)
    if total_length % 4 != 0 or len(matchsticks) < 4:
        return "false"
    target_side_length = total_length // 4
    side_lengths = [0] * 4
    matchsticks.sort(reverse=True)
    def dfs(index):
        if index == len(matchsticks):
            return all(length == target_side_length for length in side_lengths)
        for i in range(4):
            if side_lengths[i] + matchsticks[index] <= target_side_length:
                side_lengths[i] += matchsticks[index]
                if dfs(index + 1):
                    return "true"
                side_lengths[i] -= matchsticks[index]
        return "false"
    return dfs(0)
n = int(input())
matchsticks = list(map(int, input().split()))
result = makesquare(matchsticks)
print(result)
