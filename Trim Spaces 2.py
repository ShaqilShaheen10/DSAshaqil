Trim Spaces 2
Given an input string S that contains multiple words, you need to remove all the spaces present in the input string.
There can be multiple spaces present after any word.

Input Format
String s

Constraints
1 <= Length of string S <= 10^6

Output Format
Updated String

Sample Input 0
abc def g hi

Sample Output 0
abcdefghi

Sample Input 1
face prep

Sample Output 1
faceprep

Python Code:

def remove_spaces(input_string):
    words = input_string.split()
    updated_string = ''.join(words)
    return updated_string
input_string = input()
result = remove_spaces(input_string)
print(result)
