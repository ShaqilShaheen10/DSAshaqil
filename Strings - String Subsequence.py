Strings - String Subsequence
Given two strings s and t, return 1 if s is a subsequence of t, or 0 otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (i.e., "abe" is a subsequence of "abcde" while "aed" is not).

Input Format
Two strings t and s in order.

Output Format
A single integer(1 or 0)

Sample Input 0
abcde
abe

Sample Output 0
1

Sample Input 1
faceprep
aprf

Sample Output 1
0

Python Code:

def is_subsequence(s, t):
    i, j = 0, 0 
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1    
    return i == len(s)
t = input().strip()
s = input().strip()
if is_subsequence(s, t):
    print(1)
else:
    print(0)
