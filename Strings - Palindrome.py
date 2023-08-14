Strings - Palindrome
Write a program to find whether the given string is a palindrome or not without using string library functions.

Note: The string reads the same backward and forward.

Input Format
Input consists of 1 string.

Output Format
If the given string is a Palindrome display “Palindrome”, else display “Not a Palindrome”.

Sample Input 0
mam

Sample Output 0
Palindrome

Sample Input 1
string

Sample Output 1
Not a Palindrome

Python Code:

def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    left = 0
    right = len(input_str) - 1
    while left < right:
        if input_str[left] != input_str[right]:
            return False
        left += 1
        right -= 1
    return True
input_str = input().strip()
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a Palindrome")
