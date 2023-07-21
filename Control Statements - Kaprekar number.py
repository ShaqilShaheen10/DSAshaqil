Control Statements - Kaprekar number

Jaffer wanted to excel in Math. He was learning about the Kaprekar number from Meena, his Maths teacher. She gave him a few random numbers and 
asked him to find out whether they are Kaprekar number or not.
(Consider an n-digit number k. Square it and add the right n digits to the left n or n-1 digits.
 If the resultant sum is k, then k is called a Kaprekar number. For example, 9 is a Kaprekar number since 9^2 = 81 & 8 + 1 = 9,
similarly, 297 is a Kaprekar number as 297^2 = 88209 & 88 + 209 = 297 ).
Can you help Jaffer to write a program to find whether the given number is a Kaprekar number or not?

Input Format
Input consists of a single integer.

Output Format
If the output is a Kaprekar number print "Kaprekar Number" else "Not a Kaprekar Number".

Sample Input 0
45
  
Sample Output 0
Kaprekar Number
  
Sample Input 1
23
  
Sample Output 1
Not a Kaprekar Number

Python Code:

def is_kaprekar_number(num):
    square = num * num
    square_str = str(square)
    num_digits = len(str(num))
    left_part = int(square_str[:-num_digits]) if len(square_str[:-num_digits]) > 0 else 0
    right_part = int(square_str[-num_digits:])
    if left_part + right_part == num:
        return True
    else:
        return False
num = int(input())
if is_kaprekar_number(num):
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
