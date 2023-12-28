Edit Distance 13
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Input Format
First line word1
Second Line word2

Constraints
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

Output Format
Return the minimum number of operations required to convert word1 to word2.
  
Sample Input 0
horse
ros

Sample Output 0
3

Explanation 0
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Sample Input 1
intention
execution

Sample Output 1
5

Explanation 1
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Python Code:

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],   
                                  dp[i][j - 1],    
                                  dp[i - 1][j - 1])
    return dp[m][n]
word1_0 = input()
word2_0 = input()
print(minDistance(word1_0, word2_0))
