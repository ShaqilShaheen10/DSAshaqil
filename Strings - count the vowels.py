Strings - count the vowels
Write a program to count the number of vowels in the given string.

Input Format
Input consists of 1 string.

Output Format
Output print the number of Vowels.

Sample Input 0
face 

Sample Output 0
Number of vowels: 2

Sample Input 1
Antarctica

Sample Output 1
Number of vowels: 4

Python Code:

def count_vowels(s):
    vowels = "AEIOUaeiou"  
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
input_string = input().strip()
num_vowels = count_vowels(input_string)
print("Number of vowels:", num_vowels)
