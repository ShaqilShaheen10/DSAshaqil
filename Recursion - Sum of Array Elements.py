Recursion - Sum of Array Elements
Write a program to find the sum of array elements using recursion.

Input Format
The Input consists of one integer and a set of integers.
The first integer corresponds to the number of array elements.
The second Input corresponds to the array elements.
  
Output Format
The output consists of one integer that corresponds to the sum of the array elements.

Sample Input 0
5
1
2
3
4
5

Sample Output 0
15

Explanation 0
Here the sum of the array elements(1+2+3+4+5) is 15 and hence the output is 15.

Sample Input 1
2
1 
2

Sample Output 1
3

Explanation 1
Here the sum of array elements (1+2) is 3 and hence the output is 3.

Python Code:

def array_sum_recursive(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + array_sum_recursive(arr, n - 1)
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
sum_of_elements = array_sum_recursive(arr, n)
print(sum_of_elements)
