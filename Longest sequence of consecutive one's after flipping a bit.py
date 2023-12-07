Longest sequence of consecutive one's after flipping a bit
Given an integer 'n' and you are allowed to flip exactly one bit. Write a function to find the length of the longest sequence of consecutive 1’s 
you can create. Consider the size of integer to 32-bits. For example: Consider n=1775, its binary representation is 11011101111. After flipping 
the highlighted bit, we get consecutive 8 bits (of 1’s) that is 11011111111. Hence output is 8. Consider n=15, its binary representation is 01111.
After flipping the highlighted bit, we get consecutive 5 bits (of 1’s) i.e., 11111. Hence output is 5. 
Function Specification:- Give definition to: int flipBit(unsigned int n);

Input Format
Input is being fetched from the command line arguments. The only argument is an integer n.

Constraints
-10^5 to 10^5

Output Format
The output will be the length of the longest subsequence of consecutive 1’s.

Sample Input 0
1775
  
Sample Output 0
8
  
Sample Input 1
12
  
Sample Output 1
3

Python Code:

def flip_bit(n):
    binary_str = bin(n)[2:]
    max_count = 0
    current_count = 0
    previous_count = 0
    for bit in binary_str:
        if bit == '1':
            current_count += 1
        else:
            previous_count = current_count if (current_count and int(bit) == 0) else 0
            current_count = 0
        max_count = max(max_count, previous_count + current_count)
    return max_count + 1
if __name__ == "__main__":
    n = int(input())
    result = flip_bit(n)
    print(result)
