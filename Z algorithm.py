Z algorithm
Given a string text and pattern, finds all occurrences of a pattern in a text in linear time using Z algorithm

Input Format
String text
String pattern

Constraints
Time:- 1 sec

Output Format
All occurences of pattern in text

Sample Input 0
hello are you
are

Sample Output 0
Pattern found at index 6

Sample Input 1
aba aba aba
aba

Sample Output 1
Pattern found at index 0
Pattern found at index 4
Pattern found at index 8

Python Code:

def z_algorithm(text, pattern):
    concatenated = pattern + "$" + text
    n = len(concatenated)
    z_values = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z_values[i] = min(r - i + 1, z_values[i - l])
        while i + z_values[i] < n and concatenated[z_values[i]] == concatenated[i + z_values[i]]:
            z_values[i] += 1
        if i + z_values[i] - 1 > r:
            l, r = i, i + z_values[i] - 1
    occurrences = []
    for i in range(len(pattern) + 1, n):
        if z_values[i] == len(pattern):
            occurrences.append(i - len(pattern) - 1)
    return occurrences
text = input().strip()
pattern = input().strip()
occurrences = z_algorithm(text, pattern)
if occurrences:
    for index in occurrences:
        print("Pattern found at index", index)
else:
    print("Pattern not found in the text.")
