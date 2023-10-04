Quick Sort 27
Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.

Input Format
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)

Constraints
1 <= n <= 10^3

Output Format
Array elements in increasing order (separated by space)

Sample Input 0
6 
2 6 8 5 4 3

Sample Output 0
2 3 4 5 6 8

Sample Input 1
5
1 5 2 7 3

Sample Output 1
1 2 3 5 7

Python Code:

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
n = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, n - 1)
print(*arr)
