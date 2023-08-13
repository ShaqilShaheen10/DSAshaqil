Recursion - Decimal To Binary
Write a program to convert a decimal number to a binary number by recursion.

Input Format
The Input consists of an Integer

Output Format
The Output consists of the input binary form

Sample Input 0
10

Sample Output 0
1010

Sample Input 1
123

Sample Output 1
1111011

Python Code:

def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
decimal_number = int(input())
binary_representation = decimal_to_binary(decimal_number)
print(binary_representation)
