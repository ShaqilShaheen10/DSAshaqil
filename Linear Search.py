Linear Search
You have been given a integer array/list(ARR) of size N and an element X. Write a function to search this element in the given input array/list
using 'Linear Search'. Return the index of the element in the input array/list. If the element is not present in the array/list, then return -1.

Input Format
Value of your size of array
Line consists of 'n' space seperated integers representing the values present in the Array
Target element needs to find

Output Format
Sorted Array

Sample Input 0
6
1 2 3 4 5 6
2

Sample Output 0
1

Sample Input 1
6
1 2 3 4 5 6
6

Sample Output 1
5

Python Code:

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = linear_search(arr, x)
print(result)
