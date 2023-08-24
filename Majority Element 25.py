Majority Element 25
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Constraints
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
  
Output Format
Majority Element value

Sample Input 0
3
3 2 3
  
Sample Output 0
3
  
Sample Input 1
3
2 1 2
  
Sample Output 1
2

Python Code:

def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate
n = int(input())
nums = list(map(int, input().split()))
result = majority_element(nums)
print(result)
