Arrays 2D - Move all zeroes
Write a program to move all zeroes to the end of a given integer.

Input Format
The first line of input contains a number of test cases T.
For each test case, the first line of input contains a single integer of 0's and 1's.

Constraints
1 ≤ T ≤ 10
1 ≤ N ≤ 109

Output Format
The output contains a single-line integer value.

Sample Input 0
2
1010101
1000111

Sample Output 0
1111000
1111000

Sample Input 1
1
1100110

Sample Output 1
1111000

Python Code:

def move_zeroes_to_end(num):
    num_str = str(num)
    num_zeroes = num_str.count('0')
    result_str = num_str.replace('0', '') + '0' * num_zeroes
    return int(result_str)
T = int(input())
for _ in range(T):
    num = int(input())
    print(move_zeroes_to_end(num))
