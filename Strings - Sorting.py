Strings - Sorting
Write a program to sort a string in ascending order. Note: Do not use inbuilt functions.

Input Format
The input consists of the string s in a single line.

Output Format
Display the sorted string in ascending order.

Sample Input 0
faceprep

Sample Output 0
aceefppr

Sample Input 1
bac

Sample Output 1
abc

Python Code:

def sort_string(s):
    n = len(s)
    s_list = list(s)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if s_list[j] > s_list[j + 1]:
                s_list[j], s_list[j + 1] = s_list[j + 1], s_list[j]
    sorted_string = ''.join(s_list)
    return sorted_string
input_string = input().strip()
sorted_result = sort_string(input_string)
print(sorted_result)
