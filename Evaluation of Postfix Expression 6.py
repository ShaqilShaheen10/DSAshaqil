Evaluation of Postfix Expression 6
You are given with a string, you need to evaluate that string on the basis of postfix expression

Input Format
String S

Constraints
Time:- 1 sec

Output Format
Evaluated postfix expression

Sample Input 0
2 3 1 * + 9 -

Sample Output 0
-4

Sample Input 1
5 1 2 + 4 * + 3 -

Sample Output 1
14

Python Code:

def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    return stack[0]
expression_input = input()
result = evaluate_postfix(expression_input)
print(result)
