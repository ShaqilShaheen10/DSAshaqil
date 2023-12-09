Longest Happy Prefix
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

Input Format
String S

Constraints
1 <= s.length <= 105
s contains only lowercase English letters.

Output Format
Longest happy prefix

Sample Input 0
level

Sample Output 0
l

Explanation 0
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Sample Input 1
ababab

Sample Output 1
abab

Explanation 1
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Python Code:

def longest_happy_prefix(s):
    n = len(s)
    prefix_suffix_match = [0] * n
    j = 0 
    i = 1
    while i < n:
        if s[i] == s[j]:
            j += 1
            prefix_suffix_match[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix_suffix_match[j - 1]
            else:
                prefix_suffix_match[i] = 0
                i += 1
    return s[:prefix_suffix_match[-1]] if prefix_suffix_match[-1] > 0 else ""
s = input()
result = longest_happy_prefix(s)
print(result)
