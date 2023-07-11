Strings - Remove all characters in Second String that are present in First String
An online test was conducted for the students for taking up a new course. In the test, the students will be provided with two words. 
They need to remove the characters in the second word which is present in the first word and have to type the rest. Write a program to remove
all characters in the second string which are present in the first string

Input Format

Input consists of two strings.

Output Format

The output consists of one string.

Sample Input 0
Motor
Motorcycle

Sample Output 0
cycle

Explanation 0
The characters which are not present in the first string but present in the second string are a cycle and hence the output is cycle.

Sample Input 1
Bike
BikeWay

Sample Output 1
Way

Explanation 1
The character which is not present in the first string but presents in the second string is a Way and hence the output is Way

Python Code

def remove_common_chars(first_string, second_string):
    result = ""
    for char in second_string:
        if char not in first_string:
            result += char
    return result
first_string = input().strip()
second_string = input().strip()
result = remove_common_chars(first_string, second_string)
print(result)
