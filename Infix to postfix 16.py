Infix to postfix 16
Convert the given infix expression to postfix .

Input Format
String having infix expression

Output Format
Postfix expression

Sample Input 0
A+B*C+D

Sample Output 0
ABC*+D+

Sample Input 1
A+B*C/D-X

Sample Output 1
ABC*D/+X-

Python Code:

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def is_operator(char):
        return char in precedence
    def higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]
    postfix_expression = ''
    stack = []
    for char in infix_expression:
        if char.isalnum():
            postfix_expression += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression += stack.pop()
            stack.pop()  
        elif is_operator(char):
            while stack and stack[-1] != '(' and higher_precedence(stack[-1], char):
                postfix_expression += stack.pop()
            stack.append(char)
    while stack:
        postfix_expression += stack.pop()
    return postfix_expression
infix_expr_0 = input()
postfix_expr_0 = infix_to_postfix(infix_expr_0)
print( postfix_expr_0)
