Selction Sort 29
Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.

Input Format
First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format
Sorted Array

Sample Input 0
6
1 4 3 2 5 6
  
Sample Output 0
1 2 3 4 5 6
  
Sample Input 1
3
3 1 2
  
Sample Output 1
1 2 3

Python Code:

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
n = int(input())
arr = list(map(int, input().split()))
selection_sort(arr)
print(*arr)
