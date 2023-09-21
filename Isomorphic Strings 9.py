Isomorphic Strings 9
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.

Input Format
First Line string 1
Second Line string 2

Constraints
1 <= s.length <= 5 * 104
t.length == s.length

Output Format
true or false

Sample Input 0
egg
add

Sample Output 0
true

Sample Input 1
foo
bar

Sample Output 1
false

Python Code:

def isIsomorphic(s, t):
    if len(s) != len(t):
        return "false"
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return "false"
        else:
            mapping_s_to_t[char_s] = char_t
        
        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return "false"
        else:
            mapping_t_to_s[char_t] = char_s
    return "true"
s = input().strip()
t = input().strip()
print(isIsomorphic(s, t))
