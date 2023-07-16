Control Statements - Hollow square pattern

Write a program to print the hollow square pattern.

Input Format
Input consists of one integer that corresponds to the number of rows and columns.

Output Format
Output prints the hollow square pattern for the given number of rows and columns.

Sample Input 0
5
  
Sample Output 0
*****
*   *
*   *
*   *
*****
  
Explanation 0
Here the input is 5 and hence hollow square gets printed with 5 rows and 5 columns.

Sample Input 1
3
  
Sample Output 1
***
* *
***
  
Explanation 1
Here the input is 3 and hence hollow square gets printed with 3 rows and 3 columns.

Python Code:

def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

rows = int(input())
print_hollow_square(rows)
