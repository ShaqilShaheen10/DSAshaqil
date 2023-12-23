Word Break 8
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
  
Input Format
First line String S
Second line, Integer representing array length
Third Line array elements

Constraints
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Output Format
True or False

Sample Input 0
leetcode
2
leet code

Sample Output 0
true

Sample Input 1
applepenapple
2
apple pen

Sample Output 1
true

Python Code:

def word_break(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  
    for i in range(1, n + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
    return dp[n]
s = input().strip()
wordDict_length = int(input())
wordDict = input().strip().split()
result = word_break(s, wordDict)
print(str(result).lower())
