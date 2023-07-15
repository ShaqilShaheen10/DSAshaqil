Control Statements - Special number
Professor Kishore wanted the kids to learn about Special numbers. (A two-digit number is said to be a special number if the sum of sum of its digits and 
the product of its digits is equal to the number itself. For example, 19 is a special number. The digits in 19 are 1 and 9. The sum of the digits is 10 and
the product of the digits is 9. 10+9 = 19.)

Can you help Kishore to write a program to find all special numbers between 2 limits m and n (both inclusive)? Assume that m and n are two-digit numbers.

Input Format

Input consists of 2 integers m and n.
  
Output Format
Refer to the sample output for the output format.

Sample Input 0
11
19

Sample Output 0
19

Sample Input 1
12
45

Sample Output 1
19
29
39

Python Code:

def is_special(num):
    digit1 = num // 10
    digit2 = num % 10
    digit_sum = digit1 + digit2
    digit_product = digit1 * digit2
    if digit_sum + digit_product == num:
        return True
    else:
        return False
m = int(input())
n = int(input())
special_num = []
for num in range(m, n+1):
    if is_special(num):
        special_num.append(num)
for special in special_num:
    print(special)
