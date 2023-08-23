Store RainWater
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Constraints
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

Output Format
Value showing how much water we can store

Sample Input 0
12
0 1 0 2 1 0 1 3 2 1 2 1

Sample Output 0
6
  
Explanation 0
The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Sample Input 1
6
4 2 0 3 2 5

Sample Output 1
9

Python Code:

def trap(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    trapped_water = 0
    for i in range(n):
        trapped_water += max(min(left_max[i], right_max[i]) - height[i], 0)
    return trapped_water
n = int(input())
height = list(map(int, input().split()))
print(trap(height))
