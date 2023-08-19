Find duplicates from the sorted array
Given an sorted array of size N containing elements from 1 to N having only one element appearing twice. Find the duplicate element.

Input Format
First line consists of n value
Second line Consists 'n' space seperated integers representing the values present in the Array

Output Format
Print the duplicate element.

Sample Input 0
8
1 2 3 4 5 6 7 7

Sample Output 0
7

Sample Input 1
6
1 1 2 3 4 5

Sample Output 1
1

Python Code:

def find_duplicate(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    duplicate_element = find_duplicate(arr)
    print(duplicate_element)
if __name__ == "__main__":
    main()
