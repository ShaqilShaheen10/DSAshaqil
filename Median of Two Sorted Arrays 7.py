Median of Two Sorted Arrays 7
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input Format
Line consists of 'n' space seperated integers representing the values present in the Array

Constraints
nums1.length == m
nums2.length == n

Output Format
Median of two sorted arrays

Sample Input 0
2
1 2
1
3

Sample Output 0
2.0

Sample Input 1
2
1 2
2
3 4

Sample Output 1
2.5

Python Code:

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            else:
                return float(max(maxLeft1, maxLeft2))
        elif maxLeft1 > minRight2:
            high = partition1 - 1
        else:
            low = partition1 + 1
n1 = int(input())
nums1 = list(map(int, input().split()))
n2 = int(input())
nums2 = list(map(int, input().split()))
median = findMedianSortedArrays(nums1, nums2)
print(f"{median:.1f}")
