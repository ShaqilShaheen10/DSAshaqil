Daily Temperature
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
  
Input Format
First Line is the number of elemenst you want in array
Second line, give the array elements

Constraints
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

Output Format
Array within the array

Sample Input 0
8
73 74 75 71 69 72 76 73

Sample Output 0
1 1 4 2 1 1 0 0

Sample Input 1
4
30 40 50 60

Sample Output 1
1 1 1 0

Python Code:

def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
n = int(input())
temperatures = list(map(int, input().split()))
result = daily_temperatures(temperatures)
print(*result)
