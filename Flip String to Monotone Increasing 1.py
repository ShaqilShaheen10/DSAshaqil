Flip String to Monotone Increasing 1
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.

Input Format
String S

Constraints
1 <= s.length <= 105
s[i] is either '0' or '1'.

Output Format
Return the minimum number of flips to make s monotone increasing.

Sample Input 0
00110
  
Sample Output 0
1
  
Explanation 0
Explanation: We flip the last digit to get 00111.

Sample Input 1
010110
  
Sample Output 1
2
  
Explanation 1
Explanation: We flip to get 011111, or alternatively 000111.

Python Code:

def minFlipsMonoIncr(s):
    ones_count = flips = 0
    for digit in s:
        if digit == '1':
            ones_count += 1
        else:
            flips = min(flips + 1, ones_count)
    return flips
s = input()
result = minFlipsMonoIncr(s)
print(result)
