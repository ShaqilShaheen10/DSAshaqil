Control Statements - Inverted right-angled triangle

Write a program to print an inverted right-angled triangle in a star pattern.

Input Format
Input consists of one integer that corresponds to the number of pattern rows.

Output Format
Output prints the inverted right-angled triangle star pattern.

Sample Input 0
10

Sample Output 0
**********
*********
********
*******
******
*****
****
***
**
*
  
Sample Input 1
4
  
Sample Output 1
****
***
**
*

Python Code:

def print_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)
num_rows = int(input())
print_inverted_triangle(num_rows)
