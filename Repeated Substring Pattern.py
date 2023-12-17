Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Input Format
String S

Constraints
1 <= s.length <= 104
s consists of lowercase English letters.

Output Format
true or false

Sample Input 0
abab

Sample Output 0
true

Explanation 0
Explanation: It is the substring "ab" twice.

Sample Input 1
aba

Sample Output 1
false

Python Code:

def repeatedSubstringPattern(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            substring = s[:i]
            if substring * (length // i) == s:
                return "true"
    return "false"
print(repeatedSubstringPattern(input())) 
