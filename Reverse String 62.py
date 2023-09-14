Reverse String 62
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Input Format
Integer representing array size
Array having elements

Constraints
1 <= s.length <= 105

Output Format
Reversed string

Sample Input 0
5
h e l l o

Sample Output 0
o l l e h

Sample Input 1
3
w o w

Sample Output 1
w o w

Python Code:

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
n = int(input())
s = list(input().split())
reverse_string(s)
print(" ".join(s))
