Strings - String Anagram
Write a program to find whether the given string is the anagram of the first string.

Note: An anagram of a string is another string that contains the same characters, only the order of characters can be different.
Input Format

The input consists of two strings.

Output Format
The output Print "Anagram", if strings are Anagram otherwise print "Not Anagram"

Sample Input 0
eat
ate

Sample Output 0
Anagram

Sample Input 1
eat
abc

Sample Output 1
Not Anagram

Python Code:

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
input_str1 = input().strip()
input_str2 = input().strip()
if are_anagrams(input_str1, input_str2):
    print("Anagram")
else:
    print("Not Anagram")
