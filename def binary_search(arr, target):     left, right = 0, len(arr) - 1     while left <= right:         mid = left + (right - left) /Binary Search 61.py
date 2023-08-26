Binary Search 61
You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. Write a function to search this element
in the given input array/list using 'Binary Search'. Return the index of the element in the input array/list. If the element is not present in 
the array/list, then return -1.

Input Format
Value representing size of the array
Line consists of 'n' space seperated integers representing the values present in the Array
Target Element which we needs to find

Output Format
Index of that target element

Sample Input 0
3
1 2 3
0

Sample Output 0
-1

Explanation 0
0 is not present in the array, so give -1 as answer

Python Code:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
result = binary_search(arr, target)
print(result)
