Minimum Length Word 3
Find the minimum length word from the input string

Input Format
The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.

Constraints
0 <= N <= 10^6
Where N is the length of the input string.
Time Limit: 1 second

Output Format
Print the minimum word from the input string

Sample Input 0
this is mine

Sample Output 0
is
  
Sample Input 1
hello world its me

Sample Output 1
me

Python Code:

input_string = input().strip()
words = input_string.split()
min_word = None
min_length = float('inf')
for word in words:
    if len(word) < min_length:
        min_word = word
        min_length = len(word)
print(min_word)
