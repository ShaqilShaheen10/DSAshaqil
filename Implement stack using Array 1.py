Implement stack using Array 1
Write a program to implement stack using Array. Implement all the stack related functions - push, pop. print stack.

Input Format
Input consists of
n = Total number of operations
String - Operation to be performed
Integer - Elements of stack > 0

Output Format
Output consists of Integer.

Sample Input 0
10
Push
1
Pop
Push
5
Push
2
Pop
Push
7
Push
9
Push
10
Pop
Print

Sample Output 0
5
7
9

Sample Input 1
5
Push
10
Push
20
Push
30
Pop
Print

Sample Output 1
10
20

Python Code:

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    def print_stack(self):
        for element in self.stack:
            print(element)
    def is_empty(self):
        return len(self.stack) == 0
def main():
    n = int(input())
    stack = Stack()
    for _ in range(n):
        operation = input().strip()
        if operation == "Push":
            element = int(input().strip())
            stack.push(element)
        elif operation == "Pop":
            stack.pop()
        elif operation == "Print":
            stack.print_stack()
if __name__ == "__main__":
    main()
