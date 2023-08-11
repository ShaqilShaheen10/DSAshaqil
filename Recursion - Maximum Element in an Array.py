Recursion - Maximum Element in an Array
Write a program to find the maximum element in an array using recursion.

Input Format
Input consists of the size of the array and array elements

Output Format
The output prints the maximum element in an array. Refer sample input and output for formatting specifications.

Sample Input 0
6
2
5
1
7
4
2

Sample Output 0
Maximum element in the array is 7

Sample Input 1
5
23
43
14
76
98

Sample Output 1
Maximum element in the array is 98

Python Code:

def find_max(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    else:
        max_from_rest = find_max(arr, index + 1)
        if arr[index] > max_from_rest:
            return arr[index]
        else:
            return max_from_rest
def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    max_element = find_max(arr, 0)
    print("Maximum element in the array is", max_element)
if __name__ == "__main__":
    main()
