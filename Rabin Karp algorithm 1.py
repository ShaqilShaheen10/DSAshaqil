Rabin Karp algorithm 1
You are given a text and pattern string, you need to print all the ocurences of that pattern

Input Format
First line String Text
Second line String Pattern

Constraints
No

Output Format
Print occurences of the pattern

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

def find_occurrences(text, pattern):
    occurrences = []
    index = 0
    while index < len(text):
        index = text.find(pattern, index)
        if index == -1:
            break
        occurrences.append(index)
        index += 1
    return occurrences
text = input().strip()
pattern = input().strip()
occurrences = find_occurrences(text, pattern)
for index in occurrences:
    print(f"Pattern found at index {index}")
