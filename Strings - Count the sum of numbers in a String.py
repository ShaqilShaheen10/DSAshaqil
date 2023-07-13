Strings - Count the sum of numbers in a String
A game has to be played by Varun whereas he is not supposed to take the characters into account. His task is to add the numbers given in a string 
containing alphanumeric characters. If he adds the character values he will die. Help him to win the game by writing a program to print the sum of numbers

Input Format
Input consists of one string.

Output Format
The Output consists of one integer that corresponds to the sum of all numbers present in the string.

Sample Input 0
1abc23

Sample Output 0
24

Explanation 0
Here the numbers are 23 and 1 and so its sum is 24 that will get printed.

Sample Input 1
Fa33ce1

Sample Output 1
34

Explanation 1
Here the numbers are 33 and 1 and so its dum is 34 that will get printed.

Python Code:

import re
s = input()
numbers = re.findall("\d+", s)
total = sum(int(n) for n in numbers)
print(total)
