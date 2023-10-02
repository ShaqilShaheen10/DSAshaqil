Check Palindrome 15
Check whether a given String S is a palindrome using recursion. Return true or false.

Input Format
String S

Constraints
0 <= |S| <= 1000
where |S| represents length of string S.

Output Format
true or false

Sample Input 0
racecar
  
Sample Output 0
true
  
Sample Input 1
face
  
Sample Output 1
false

Python Code:

def is_palindrome(s):
    if len(s) <= 1:
        return "true"
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return "false"
input_string = input().strip()
result = is_palindrome(input_string)
print(result)
