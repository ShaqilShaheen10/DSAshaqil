Reverse WordWise
Akhil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that
each word in the sentence is reversed.

Input Format
String in a single line

Constraints
0 <= N <= 10^6
Where N is the length of the input string.
Time Limit: 1 second

Output Format
Word wise reversed string in a single line

Sample Input 0
Welcome to Face Prep

Sample Output 0
emocleW ot ecaF perP

Sample Input 1
Always indent your code

Sample Output 1
syawlA tnedni ruoy edoc

Python Code:

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_word = word[::-1] 
        reversed_words.append(reversed_word)
    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)
input_sentence = input()
reverse_words(input_sentence)
