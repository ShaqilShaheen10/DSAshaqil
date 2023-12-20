Split Array Largest Sum
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Input Format
First Line array size
Second Line array elements
Third line K value

Constraints
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

Output Format
Return the minimized largest sum of the split.

Sample Input 0
5
7 2 5 10 8
2

Sample Output 0
18

Sample Input 1
5
1 2 3 4 5
2

Sample Output 1
9

Python Code:

def splitArray(nums, k):
    def feasible(mid):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                count += 1
                total = num
                if count > k:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
n = int(input())
nums = list(map(int, input().split()))
k = int(input())
result = splitArray(nums, k)
print(result)
