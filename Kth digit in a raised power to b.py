Kth digit in a raised power to b
Given three numbers a, b and k, find k-th digit in a^b from right side

Input Format
First line Integer a Second line Integer b Third line Integer k

Constraints
no

Output Format
find k-th digit in a^b from right side

Sample Input 0
3
3
1

Sample Output 0
7

Explanation 0
Explanation: 3^3 = 27 for k = 1. First digit is 7 in 27

Sample Input 1
5
2
2

Sample Output 1
2

Explanation 1
Explanation: 5^2 = 25 for k = 2. First digit is 2 in 25

Python Code:

def kth_digit_of_power(a, b, k):
    result = str(a ** b)
    if k <= len(result):
        return int(result[-k])
    else:
        return 0
a = int(input())
b = int(input())
k = int(input())
print(kth_digit_of_power(a, b, k))
