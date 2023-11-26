Count Number of Nodes in tree
You are given the root node of a binary tree.Count the number of nodes present.

Input Format
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or 
right node data exist for root, it will not be a part of the node data.

Constraints
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Output Format
The only line of output prints the number of nodes in Binary Tree

Sample Input 0
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 0
7

Sample Input 1
5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1

Sample Output 1
6

Python Code:

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert_level_order(arr, root, i, n):
    if i < n and arr[i] != -1:
        temp = Node(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
elements = list(map(int, input().strip().split()))
root_node = None
root_node = insert_level_order(elements, root_node, 0, len(elements))
node_count = count_nodes(root_node)
print(node_count)
