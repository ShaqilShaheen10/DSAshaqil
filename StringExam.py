You are given a string S containing lowercase English letters. Your task is to calculate the minimum number of 
letters that need to be removed in order to make it possible to build a palindrome from the remaining letters.
When building the palindrome, you can rearrange the remaining letters in any way.

A palindrome is a string that reads the same both forwards and backwards. Some examples of palindromes are: 
"kayak", "radar", "mom".

Write a function:

def solution (5)

which, given a string of length N, returns the minimum number of letters that
need to be removed.

Examples:

1. Given S = "ervervige", your function should return 2. After removing 
the letter "g" and one "e", we may create a word "reviver", which is a palindrome.

2. Given S = "aaabab", your function should return 0. We may create a word 
"aabbaa", which is a palindrome and uses all of the letters.

3. Given S = "x", your function should return 0. String "x" is a palindrome itself,

so we do not have to delete any letter.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..200,000] .S contains only lowercase English letters.

Python code
                            
def solution(S):
    letter_count = {}
    for char in S:
        letter_count[char] = letter_count.get(char, 0) + 1

    odd_occurrences = sum(count % 2 for count in letter_count.values())
    return max(0, odd_occurrences - 1)
