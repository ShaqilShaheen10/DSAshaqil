Missing number in series
Given an array that represents elements of an arithmetic progression. One element is missing in the progression, find the missing number. The first and last element 
will not be the missing number.

Input Format
The first line of input consists of size of an array. The second line of input consists of elements of an array separated by space.

Constraints
1 <= N <= 1000 1 <= k <= 50000

Output Format
The output consists of the missing number in the series.

Sample Input 0
5
1 5 7 9 11

Sample Output 0
3

Sample Input 1
5
1 3 7 9 11

Sample Output 1
5

Python Code:

def findMissingNumber(arr):
    common_diff = (arr[-1] - arr[0]) // len(arr)
    expected_next = arr[0]
    for num in arr:
        if num == expected_next:
            expected_next += common_diff
        else:
            return expected_next
n = int(input())
arr = list(map(int, input().split()))
missing_number = findMissingNumber(arr)
print(missing_number)
