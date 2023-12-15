Reverse Bits 7
Reverse bits of a given integer N
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 
and the output represents the signed integer -1073741825.

Input Format
Take Integer Input
  
Constraints
The input must be a binary string of length 32
  
Output Format
Tell the decimal number after reversing bits
  
Sample Input 0
43261596
  
Sample Output 0
964176192
  
Explanation 0
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which
its binary representation is 00111001011110000010100101000000.

Sample Input 1
43261500
  
Sample Output 1
1014507840
  
Explanation 1
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its
binary representation is 10111111111111111111111111111111.

Python Code:

def reverse_bits(n):
  result = 0
  for i in range(32):
    bit = (n >> i) & 1
    result |= (bit << (31 - i))
  return result
n = int(input())
reversed_n = reverse_bits(n)
print(reversed_n)
