Palindrome String 18
Given a string, determine if it is a palindrome, considering only alphanumeric characters.

Input Format
The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.

Constraints
0 <= N <= 10^6
Where N is the length of the input string.
Time Limit: 1 second

Output Format
The only line of output prints either 'true' or 'false'.

Sample Input 0
abba

Sample Output 0
true

Sample Input 1
aba

Sample Output 1
true

Python Code:

def is_palindrome(s):
    cleaned_s = ''.join(c for c in s if c.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]
s = input()
if is_palindrome(s):
    print("true")
else:
    print("false")
