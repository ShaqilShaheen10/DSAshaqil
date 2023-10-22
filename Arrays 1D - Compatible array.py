Arrays 1D - Compatible array
Two arrays are said to be compatible if they are of the same size and if the ith element in the first array is greater than or equal to the ith element in the
second array for all the values of i. Write a program to find whether 2 arrays are compatible or not.

Input Format

Input consists of 2n+2 integers. The first integer corresponds to ‘n1’, the size of the first array. The next ‘n1’ integers correspond to the elements 
in the first array. The next (n+1) integer corresponds to 'n2', the size of the second array. The last 'n2' integers correspond to the elements in the second array.

Output Format
The output is any one of the two strings "Compatible" or "Incompatible"

Sample Input 0
5
2
3
6
8
1
5
1
1
1
1
1

Sample Output 0
Compatible

Sample Input 1
5
2
3
6
8
1
5
1
1
1
1
2

Sample Output 1
Incompatible

Python Code:

def are_arrays_compatible(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] < arr2[i]:
            return False

    return True


if __name__ == "__main__":
    n1 = int(input())
    array1 = [int(input()) for _ in range(n1)]

    n2 = int(input())
    array2 = [int(input()) for _ in range(n2)]

    if are_arrays_compatible(array1, array2):
        print("Compatible")
    else:
        print("Incompatible")
