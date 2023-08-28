Insertion sort 38
Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Insertion Sort'.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Constraints
1 <= t <= 10^2
0 <= N <= 10^3
Time Limit: 1 sec

Output Format
Sorted Array

Sample Input 0
3
1 9 8

Sample Output 0
1 8 9

Sample Input 1
7
2 13 4 1 3 6 28

Sample Output 1
1 2 3 4 6 13 28

Python Code:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
n = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr)
print(*arr)
