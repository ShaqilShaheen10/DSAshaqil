Strings - Reverse each word of a string
Write the program to reverse each word of a string.

Input Format
Input consists of one string

Output Format
The output consists of one string (reverse of the input string)

Sample Input 0
Hello World

Sample Output 0
World Hello

Sample Input 1
welcome to face

Sample Output 1
face to welcome

Python Code:

def reverse_each_word(input_str):
    words = input_str.split()
    reversed_words = [word[::1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
input_str = input()
reversed_order_str = ' '.join(input_str.split()[::-1])
output_str = reverse_each_word(reversed_order_str)
print(output_str)
