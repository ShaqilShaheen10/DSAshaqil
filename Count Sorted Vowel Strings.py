Count Sorted Vowel Strings
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Input Format
First Line Integer N

Constraints
1 <= n <= 50

Output Format
Return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

Sample Input 0
1

Sample Output 0
5

Sample Input 1
2

Sample Output 1
15

Python Code:

def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    dp = [[0] * 5 for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i-1][:j+1])
    result = sum(dp[n-1])
    return result
n1 = int(input())
print(count_sorted_vowel_strings(n1))
