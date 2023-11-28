Combinational Sum 1
Given an array of positive integers arr[] and an integer x, The task is to find all unique combinations in arr[] where the sum is equal to x.
The same repeated number may be chosen from arr[] an unlimited number of times. Elements in a combination (a1, a2, …, ak) must be printed in non-descending order. 
(ie, a1 <= a2 <= … <= ak). If there is no combination possible print “Empty”.

Input Format
First line array size
Second line array elements
Third line target value

Constraints
Time:- 1 Sec

Output Format
Pairs in different lines

Sample Input 0
4
2 3 6 7
7

Sample Output 0
2 2 3
7

Sample Input 1
3
2 3 5
8

Sample Output 1
2 2 2 2
2 3 3
3 5

Python Code:

def find_combinations(arr, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path.copy())
            return
        for i in range(start, len(arr)):
            if target < arr[i]:
                continue
            path.append(arr[i])
            backtrack(i, target - arr[i], path)
            path.pop()
    result = []
    arr.sort()
    backtrack(0, target, [])
    return result
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
combinations = find_combinations(arr, x)
if not combinations:
    print("Empty")
else:
    for combination in combinations:
        print(" ".join(map(str, combination)))
