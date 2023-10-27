Check if number is jumbled or not
Write a program to check if a given integer is jumbled or not. A number is said to be Jumbled if for every digit, its neighbours digit differs by max 1.

Input Format
Integer N

Output Format
true or false

Sample Input 0
1223

Sample Output 0
true

Sample Input 1
6767

Sample Output 1
true

Python Code:

def is_jumbled(n):
    n = str(n)
    for i in range(len(n) - 1):
        if abs(int(n[i]) - int(n[i + 1])) > 1:
            return "false"
    return "true"
n = int(input())
print(is_jumbled(n))
