Strings - First Non-repeating Character
Lee conducted a word game for his colleagues. The game is everyone should say a word that should not have any repeating characters in it. If a single character 
is repeated then the particular person can't continue the game. Lee finds it difficult to disqualify the person from the game since he is not able to find the 
nonrepetitive character for all the words. Help him to find the winner of the game by writing a program to find the first element which is non -repetitive i.e 
that element must not be present anywhere else in the string.

Input Format

The first line of the input consists of a string.

Output Format
The output displays a character that is non-repetitive. If all the characters in an input string are repetitive, then display All characters are repetitive.

Sample Input 0
teeterson 

Sample Output 0
r

Explanation 0
Here in the word teeterson the first non-repeating character is r and hence it prints r.

Sample Input 1
goog

Sample Output 1
All the characters are repetitive

Explanation 1
Here in the word goog all the characters are repetitive and hence it prints All the characters are repetitive.

Python Code:

def find_first_non_repetitive(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return "All the characters are repetitive"
input_string = input()
result = find_first_non_repetitive(input_string)
print(result)
