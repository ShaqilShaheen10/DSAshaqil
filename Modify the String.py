Modify the String

Given a string input_str of length n, choose any character that occurs at least twice and delete any one occurrence. Repeat this until all remaining 
characters are distinct. Return the lexicographically maximum string that can be formed this way.

Example
input_str = "aabcb"

The length of the string, n = 5. Some of the strings that can be formed are:

• "acb" - delete the first occurrences of 'a' and 'b'

"abc" - delete the first occurrence of 'a' and the second occurrence of 'b'

It can be proven that the lexicographically maximum string that can be obtained is "acb".
getString has the following parameters: string input str: a string of length n

Sample Case 0

STDIN
FUNCTION
input_str = "abacaba"

Sample Output
cba

Explanation

The length of the string n = 7. The strings that can be formed are: "abc", "bca", "cab", "acb", "cba" and "bac". The lexicographically maximum is "cba"

Python Code:

def getString(input_str):
    char_count = {}
    
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    result = []
    for char in input_str:
        if char_count[char] > 1:
            char_count[char] -= 1
        else:
            result.append(char)
    
    return ''.join(result)
input_str = "abacaba"
result = getString(input_str)
print(result)  # Output: "cba"
