Largest Number 27
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Input Format
First Line array size
Second line array eleemnts

Constraints
1 <= nums.length <= 100
0 <= nums[i] <= 109

Output Format
Largest Number

Sample Input 0
2
10 2

Sample Output 0
210

Sample Input 1
5
3 30 34 5 9

Sample Output 1
9534330

Python Code:

from functools import cmp_to_key
def largestNumber(nums):
    def compare(x, y):
        return int(y + x) - int(x + y)
    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(compare))
    result = ''.join(nums_str)
    result = result.lstrip('0')
    return result if result else '0'
n = int(input())
nums = list(map(int, input().split()))
result = largestNumber(nums)
print(result)
