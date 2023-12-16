Single Number 9
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
                                                                     
Input Format
First Line array size
Second Line elements of array

Constraints
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
                                       
Output Format
Unique Number present in the array

Sample Input 0
3
2 2 1

Sample Output 0
1

Sample Input 1
5
2 2 3 3 4

Sample Output 1
4

Python Code:

def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
n = int(input())
nums = list(map(int, input().split()))
print(find_single_number(nums))
