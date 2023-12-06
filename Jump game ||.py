Jump game ||
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Input Format
First Line aray size
Second line array elements

Constraints
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

Output Format
Return the minimum number of jumps to reach nums[n - 1]

Sample Input 0
5
2 3 1 1 4

Sample Output 0
2

Explanation 0
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Sample Input 1
5
2 3 0 1 4

Sample Output 1
2

Python Code:

def min_jumps(nums):
    n = len(nums)
    if n == 1:
        return 0
    jumps = 1
    current_max = nums[0]
    next_max = nums[0]
    for i in range(1, n):
        if i == n - 1:
            return jumps
        next_max = max(next_max, i + nums[i])
        if i == current_max:
            jumps += 1
            current_max = next_max
    return jumps
n = int(input())
nums = list(map(int, input().split()))
result = min_jumps(nums)
print(result)
