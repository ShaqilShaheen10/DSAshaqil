LCA of Binary tree
Given a binary tree and data of two nodes, find 'LCA' (Lowest Common Ancestor) of the given two nodes in the binary tree.
LCA
LCA of two nodes A and B is the lowest or deepest node which has both A and B as its descendants.
It is defined that each node is a descendant to itself, so, if there are two nodes X and Y and X has a direct connection from Y, then Y is the lowest common ancestor.
Example:
Note:
If out of 2 nodes only one node is present, return that node.
If both are not present, return -1.

Input Format
The first line of input contains data of the nodes of the tree in level order form. The data of the nodes of the tree is separated by space.
If any node does not have left or right child, take -1 in its place. Since -1 is used as an indication whether the left or right nodes exist, therefore,
it will not be a part of the data of any node.
The following line of input contains two integers, denoting the value of data of two nodes of given binary tree.

Constraints
Time:- 1 Sec

Output Format
The first and only line of output contains the data associated with the lowest common ancestor node.
  
Sample Input 0
5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1
2 10

Sample Output 0
10

Sample Input 1
5 10 6 2 3 -1 -1 -1 -1 -1 9 -1 -1
2 6

Sample Output 1
5

Python Code:

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
def find_lca(root, node1, node2):
    if not root:
        return None
    if root.val == node1 or root.val == node2:
        return root.val
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)
    if left_lca is not None and right_lca is not None:
        return root.val
    elif left_lca is not None:
        return left_lca
    else:
        return right_lca
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)
        if arr[i] != -1:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root
tree_values = list(map(int, input().split()))
node1, node2 = map(int, input().split())
root = build_tree(tree_values)
result = find_lca(root, node1, node2)
print(result)
