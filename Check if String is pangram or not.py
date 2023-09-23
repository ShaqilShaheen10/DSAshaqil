Check if String is pangram or not
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Input Format
String S

Constraints
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

Output Format
true or false

Sample Input 0
thequickbrownfoxjumpsoverthelazydog

Sample Output 0
true

Explanation 0
sentence contains at least one of every letter of the English alphabet.

Sample Input 1
leetcode

Sample Output 1
false


Python Code:

def is_pangram(sentence):
    unique_letters = set()
    for char in sentence:
        if 'a' <= char <= 'z':
            unique_letters.add(char)
        if len(unique_letters) == 26:
            return "true"
    return "false"
sentence = input()
output = is_pangram(sentence)
print(output) 
