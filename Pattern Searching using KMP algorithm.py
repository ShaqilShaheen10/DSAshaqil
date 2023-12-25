Pattern Searching using KMP algorithm
Given a string text and pattern, finds all occurrences of a pattern in a text in linear time using KMP algorithm

Input Format
String text
String pattern

Constraints
Time:- 1 sec

Output Format
Pattern found at which index

Sample Input 0
ABABDABACDABABCABAB
AB

Sample Output 0
Pattern found at index 0
Pattern found at index 2
Pattern found at index 5
Pattern found at index 10
Pattern found at index 12
Pattern found at index 15
Pattern found at index 17

Sample Input 1
ABABDABACDABABCABAB
A

Sample Output 1
Pattern found at index 0
Pattern found at index 2
Pattern found at index 5
Pattern found at index 7
Pattern found at index 10
Pattern found at index 12
Pattern found at index 15
Pattern found at index 17

Python Code:

def build_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    return lps
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = build_lps_array(pattern)
    result = []
    i, j = 0, 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result
text = input()
pattern = input()
occurrences = kmp_search(text, pattern)
for index in occurrences:
    print(f"Pattern found at index {index}")
