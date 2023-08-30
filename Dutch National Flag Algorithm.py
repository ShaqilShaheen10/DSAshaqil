Dutch National Flag Algorithm
You have been given a integer array/list(ARR) of size N. In the array you are only having 0, 1 and 2 elements. Write a function to sort the array using this algorithm.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format
Return Sorted Array

Sample Input 0
3
0 1 0
  
Sample Output 0
0 0 1
  
Sample Input 1
9
0 0 1 1 2 2 2 0 1

Sample Output 1
0 0 0 1 1 1 2 2 2

Python Code:

def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sortArray(arr)
print(" ".join(map(str, sorted_arr)))
