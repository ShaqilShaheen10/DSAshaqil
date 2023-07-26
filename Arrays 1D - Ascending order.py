Arrays 1D - Ascending order

Kailash and his daughter Keerthana were arguing about who is the smartest person in the family. Kailash who is a world-known Computer Engineer 
asked Keerthana who has not yet completed college to write a program to sort the given array in ascending order. Can you help Keerthana?

Input Format
Input consists of 1 integer and 1 array. The integer corresponds to the size of the array.

Output Format
The output consists of an array of elements after sorting.

Sample Input 0
5
54
68
25
14
74

Sample Output 0
The Sorted array is:
14
25
54
68
74

Sample Input 1
4
6
7
8
3

Sample Output 1
The Sorted array is:
3
6
7
8

Explanation 1
Here we can compare the 1st value(6)with all the other values,6 is greater than 3 and hence 6 will get printed in the second position.
Repeat the same process for all the remaining values to get the output in sorted order.

Python Code:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
size = int(input())
arr = []
for _ in range(size):
    arr.append(int(input()))
sorted_arr = bubble_sort(arr)
print("The Sorted array is:")
for num in sorted_arr:
    print(num)
