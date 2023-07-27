Arrays 1D - Remove duplicate elements

Jack and John were investigating a murder and the murderer was Ms.Isha Adler. She wanted Jack to find her by solving the puzzles. Jack was able to solve all 
but one. The last task was to write a program to remove duplicate elements from an array. Can you help Jack?

Input Format
Input consists of 1 integer and 1 array. The first integer corresponds to the size of the array. The next integers correspond to the elements in the array.

Output Format
The output consists of an array with no duplicate elements.

Sample Input 0
5
1
2
2
3
4

Sample Output 0
1
2
3
4

Explanation 0
Here, among the array elements, 1 is repeated twice, removing the duplicate ones we can print the remaining array elements. Hence the output is 1 5

Sample Input 1
4
3
2
1
2

Sample Output 1
3
2
1

Python Code:

def remove_duplicates(arr):
    unique_elements = set()
    result = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            result.append(element)
    return result
size = int(input())
array = []
for _ in range(size):
    array.append(int(input()))
for element in remove_duplicates(array):
    print(element)
