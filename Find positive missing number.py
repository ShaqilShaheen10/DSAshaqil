Find positive missing number
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format
First positive missing number

Sample Input 0
3
1 2 0

Sample Output 0
3

Sample Input 1
4
-1 2 3 4

Sample Output 1
1

Explanation 1
2 is in the array but 1 is missing.

Python Code:

def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
n = int(input())
nums = list(map(int, input().split()))
print(firstMissingPositive(nums))
