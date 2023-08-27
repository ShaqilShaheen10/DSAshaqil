Bubble Sort
Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble Sort'.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format
Give Sorted Array

Sample Input 0
3
3 1 2
  
Sample Output 0
1 2 3
  
Sample Input 1
5
4 3 2 2 1
  
Sample Output 1
1 2 2 3 4

Python Code:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
n = int(input())
arr = list(map(int, input().split()))
bubble_sort(arr)
print(*arr)
