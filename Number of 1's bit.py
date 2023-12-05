Number of 1's bit
Write a function that takes the decimal representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect 
your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Input Format
Take Integer N

Output Format
Number of 1's bit

Sample Input 0
11

Sample Output 0
3

Sample Input 1
395

Sample Output 1
5

Python Code:

def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
sample_input_0 = int(input())
print(hamming_weight(sample_input_0))
