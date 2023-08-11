Recursion - Compute a^n
When the inventor of the game showed the game to the emperor of India, the emperor was so impressed by the new game, that he said to the man "Name your reward!" 
The man responded, "Oh emperor, my wishes are simple. I only wish for this. Give me one grain of rice for the first square of the chessboard, 2^2 for the next
square, 3^3 for the next, 4^4 for the next, and so on for all 64 squares". The emperor agreed, amazed that the man had asked for such a small reward. After a week,
his treasurer came back and informed him that the reward would add up to an astronomical sum, far greater than all the rice that could conceivably be produced 
in many many centuries. The Emperor wanted to check it for himself. Can you help the Emperor to write a program to compute a^n (a power n) using recursion?

Input Format
The input consists of two integers a and n.

Output Format
Refer to sample output.

Sample Input 0
2
8
  
Sample Output 0
The value of 2 power 8 is 256

Explanation 0
In this case value of a and n is 2 and 8 respectively. Then the answer will be like this 2 ^ 2 ^ 2 ^ . . . . (8 times ) = 256.

Sample Input 1
3
1

Sample Output 1
The value of 3 power 1 is 3

Explanation 1
In this case values of a and n are 3 and 1 respectively. Then the answer will be like this 3 ^ 1 ^ = 1.

Python Code:

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = int(input())
n = int(input())
result = power(a, n)
print(f"The value of {a} power {n} is {result}")
