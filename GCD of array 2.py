GCD of array 2
Given an array of numbers, find GCD of the array elements

Input Format
First Line array size
Second Line array elements

Constraints
No

Output Format
GCD of elements of array

Sample Input 0
5
2 4 6 8 16

Sample Output 0
2

Sample Input 1
3
1 2 3

Sample Output 1
1

Python Code:

import math
array_size = int(input())
array_elements = list(map(int, input().split()))
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
result = array_elements[0]
for i in range(1, array_size):
    result = gcd(result, array_elements[i])
print(result)
