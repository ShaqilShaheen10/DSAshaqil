Manacher's Algorithm
Given a string, find the longest substring which is palindrome.

Input Format
String s

Output Format
Longest palindromic string

Sample Input 0
babcbabcbaccba

Sample Output 0
abcbabcba

Sample Input 1
abaaba

Sample Output 1
abaaba

Python Code:

def longest_palindrome_bruteforce(s):
  n = len(s)
  longest = ""
  for start in range(n):
    for end in range(start + 1, n + 1):
      substring = s[start:end]
      if substring == substring[::-1] and len(substring) > len(longest):
        longest = substring
  return longest
test_string = input()
longest_palindrome = longest_palindrome_bruteforce(test_string)
print(longest_palindrome)
