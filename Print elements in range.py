Print Elements in Range
Given a Binary Search Tree and two integers k1 and k2, find and print the elements which are in range k1 and k2 (both inclusive).
Print the elements in increasing order.

Input Format
First line array size
Second line array elements
Third line k1 value
Fourth line k2 value

Constraints
Time :- 1 Sec

Output Format
The first and only line of output prints the elements which are in range k1 and k2 (both inclusive). Print the elements in increasing order.

Sample Input 0
6
8 5 10 2 6 7
6
10

Sample Output 0
6 7 8 10

Sample Input 1
1
1
2
5

Python Code:

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def print_in_range(root, k1, k2):
    if root is not None:
        print_in_range(root.left, k1, k2)
        if k1 <= root.val <= k2:
            print(root.val, end=" ")
        print_in_range(root.right, k1, k2)
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    k1 = int(input())
    k2 = int(input())
    root = None
    for element in elements:
        root = insert(root, element)
    print_in_range(root, k1, k2)
