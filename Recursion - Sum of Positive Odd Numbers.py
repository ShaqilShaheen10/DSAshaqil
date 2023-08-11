Recursion - Sum of Positive Odd Numbers
Write a program to find the sum of the positive odd numbers present in an array using recursion.

Input Format
The first integer input represents the size of the array (n), next n lines consist of values present in the array.

Output Format
The output prints the sum of positive odd numbers in an array. Refer to the sample output for formatting specifications.

Sample Input 0
3
1
1
1

Sample Output 0
Sum = 3

Sample Input 1
5
1
2
3
4
5

Sample Output 1
Sum = 9

Python Code:

def sum_positive_odd(arr, index):
    if index < 0:
        return 0
    current_number = arr[index]
    if current_number > 0 and current_number % 2 == 1:
        return current_number + sum_positive_odd(arr, index - 1)
    else:
        return sum_positive_odd(arr, index - 1)
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
result = sum_positive_odd(array, n - 1)
print("Sum =", result)
