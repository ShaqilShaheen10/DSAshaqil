Replace X 2
Given a string, compute recursively a new string where all 'x' chars have been removed.

Input Format
String S

Constraints
1 <= |S| <= 10^3 where |S| represents the length of string S.

Output Format
Modified string

Sample Input 0
xaxb

Sample Output 0
ab

Sample Input 1
abc

Sample Output 1
abc

Python Code:

def remove_x(s):
    if len(s) == 0:
        return ""
    if s[0] == 'x':
        return remove_x(s[1:])
    else:
        return s[0] + remove_x(s[1:])
input_string = input()
modified_string = remove_x(input_string)
print(modified_string)
