Binary Palindrome
Write a program to check whether it’s a binary palindrome or not.

Input Format
The input consist of an integer

Constraints
Time complexity Constraint : O(log n)

Output Format
Print "Yes" or "No"

Sample Input 0
9

Sample Output 0
Yes

Sample Input 1
8

Sample Output 1
No

Python Code:

def is_binary_palindrome(num):
    binary_representation = bin(num)[2:] 
    reversed_binary = binary_representation[::-1]
    return binary_representation == reversed_binary
if __name__ == "__main__":
    num = int(input().strip())

    if is_binary_palindrome(num):
        print("Yes")
    else:
        print("No")
