Two Sum 67
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
Third line contains an integer 'X'.

Constraints
Time complexity Constraint : O(n)

Output Format
Two integer values indicating the indices of the two numbers whose sum is equal to the target value.

Sample Input 0
4
2 7 11 15
9

Sample Output 0
0 1

Sample Input 1
3
3 2 4
6

Sample Output 1
1 2

Python Code:

def twoSum(nums, target):
    complements = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]
        complements[num] = i
    return []
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
result = twoSum(nums, target)
print(*result)
