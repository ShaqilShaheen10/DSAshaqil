Replace character 2
Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string.

Input Format
Line 1 : Input String S
Line 2 : Character c1 and c2 (separated by space)

Constraints
1 <= Length of String S <= 10^6

Output Format
Updated string

Sample Input 0
abacd
a x

Sample Output 0
xbxcd

Sample Input 1
abacd
a a

Sample Output 1
abacd

Python Code:

S = input()
c1, c2 = input().split()
updated_string = S.replace(c1, c2)
print(updated_string)
