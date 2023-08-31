Minimum Moves to Equal Array Elements
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.

Input Format
First line array size
Second line array elements

Constraints
n == nums.length
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Output Format
Moves required to make array equal

Sample Input 0
3
1 2 3

Sample Output 0
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3] => [2,2,3] => [2,2,2]

Sample Input 1
4
1 10 2 9

Sample Output 1
16

Python Code:

def min_moves_to_equal(nums):
    nums.sort()
    median = nums[len(nums) // 2] 
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves
n = int(input())
nums = list(map(int, input().split()))
result = min_moves_to_equal(nums)
print(result)
