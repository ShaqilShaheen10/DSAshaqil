Maximum Sum Path of Binary Tree
You are given a binary tree having 'N' nodes. Each node of the tree has an integer value. Your task is to find the maximum possible sum of a simple path
between any two nodes (possibly same) of the given tree.
A simple path is a path between any two nodes of a tree, such that no edge in the path is repeated twice. Sum of a simple path is defined as the summation
of all node values in a path.

Input Format
The only line of each test case contains elements in the level order form. The line consists of values of nodes separated by a single space. In case a node is null,
we take -1 on its place.

Constraints
Time:- 1 Sec

Output Format
Print the output .

Sample Input 0
1 2 3 4 -1 -1 -1 -1 -1

Sample Output 0
10

Sample Input 1
2 4 -1 3 6 -1 -1 -1 -1

Sample Output 1
13

Python Code:

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def max_path_sum(root):
    if not root:
        return 0
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))
        max_sum = max(max_sum, left_sum + right_sum + node.value)
        return max(left_sum, right_sum) + node.value
    max_sum = float('-inf')
    dfs(root)
    return max_sum
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes.pop(0))
    queue = [root]
    while queue:
        current = queue.pop(0)
        left_value = nodes.pop(0)
        if left_value != -1:
            current.left = TreeNode(left_value)
            queue.append(current.left)
        right_value = nodes.pop(0)
        if right_value != -1:
            current.right = TreeNode(right_value)
            queue.append(current.right)
    return root
input_nodes_0 = list(map(int,input().split()))
root_0 = build_tree(input_nodes_0)
result_0 = max_path_sum(root_0)
print(result_0)  
