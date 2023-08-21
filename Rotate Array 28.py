Rotate Array 28
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input Format
First line contains the value of size of your array
Line consists of 'n' space seperated integers representing the values present in the Array
Third line having the K value, how much you want to rotate

Constraints
1 <= nums.length <= 10^5
-231 <= nums[i] <= 231 - 1
0 <= k <= 10^5

Output Format
Rotated Array

Sample Input 0
7
1 2 3 4 5 6 7
3

Sample Output 0
5 6 7 1 2 3 4

Explanation 0
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Sample Input 1
4
-1 -100 3 99
2

Sample Output 1
3 99 -1 -100

Explanation 1
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Python Code:

def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
size = int(input())
nums = list(map(int, input().split()))
k = int(input())
rotated_nums = rotate_array(nums, k)
print(' '.join(map(str, rotated_nums)))
