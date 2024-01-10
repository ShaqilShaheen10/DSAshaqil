Balanced Parenthesis
For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if 
the bracket which opens last, closes first.

Input Format
Expression: (()())
Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
You need to return a boolean value indicating whether the expression is balanced or not.
Note:
The input expression will not contain spaces in between.

Constraints
1 <= N <= 10^7
Where N is the length of the expression.
Time Limit: 1sec

Output Format
The only line of output prints 'true' or 'false'.

Sample Input 0
(()()())

Sample Output 0
true

Sample Input 1
()()(()
     
Sample Output 1
false

Python Code:

def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "false"
            stack.pop()
        else:
            return "true"
    return str(not stack).lower()
expression_0 = input().strip()
result_0 = is_balanced(expression_0)
print(result_0)
