Merge Sort 36
Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble Sort'.

Input Format
First line consists of array size
Second line having the elements of array

Constraints
0 <= N <= 10^3
Time Limit: 1 sec

Output Format
Sorted Array

Sample Input 0
4
4 3 2 1

Sample Output 0
1 2 3 4

Sample Input 1
6
3 2 1 6 5 4

Sample Output 1
1 2 3 4 5 6

Python Code:

N = int(input())
ARR = list(map(int, input().split()))
for i in range(N):
    for j in range(0, N - i - 1):
        if ARR[j] > ARR[j + 1]:
            ARR[j], ARR[j + 1] = ARR[j + 1], ARR[j]
print(' '.join(map(str, ARR)))
