Control Statements - Collatz problem
Chander started working for Bing and he wanted him to write a program to generate Collatz Sequence. The rules for generating the Collatz sequence are: If n is even,
n = n / 2. If n is odd, n = 3n + 1.
For example, if the starting number is 5 the sequence is: 5 -> 16 -> 8 -> 4 -> 2 -> 1 It has been proved for almost all integers, that the repeated application
of the above rule will result in a sequence that ends in 1.

Input Format
The input is an integer 'n' which denotes the first term of the sequence.

Output Format
As output, print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1.

Sample Input 0
18

Sample Output 0
18
9
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
20

Sample Input 1
1

Sample Output 1
1
0

Python Code:

def generate_collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
start_number = int(input())
collatz_sequence = generate_collatz_sequence(start_number)
for num in collatz_sequence:
    print(num)    
def apply_rule(n):
    sequence = [n]
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        count += 1
    return sequence, count
input_number = start_number
sequence, count = apply_rule(input_number)
print(count)
