Arrays 1D - Count distinct elements

Harish and Rajesh were developing a plan to find the ideal woman for Sheldon Cooper. There were puzzles, translations, and questions to check a person's
intelligence. One such question was to come up with a program to count the number of distinct elements in an array. Harini is a postdoctoral researcher
and a former graduate student of Caltech who is a huge fan of Sheldon's work and she wanted to impress Sheldon by writing a program to count the number of
distinct element in an array. Can you help Harini?

Input Format
Input consists of 1 integer and 1 array. The first integer corresponds to the size of the array.

Output Format
The output prints the number of distinct element in an array.

Sample Input 0
5
1
2
3
3
4

Sample Output 0
There are 4 distinct element in the array.

Explanation 0
Since there are 4 distinct elements it will print There are 4 distinct element in the array.

Sample Input 1
5
1
1
2
3
3

Sample Output 1
There are 3 distinct element in the array.

Explanation 1
Since there are 3 distinct element it will print There are 3 distinct element in the array.

Python Code:

def count_distinct_elements(arr):
    distinct_set = set(arr)
    num_distinct_elements = len(distinct_set)
    return num_distinct_elements
size = int(input())
array = []
for _ in range(size):
    array.append(int(input()))
result = count_distinct_elements(array)
print(f"There are {result} distinct element in the array.")
