Right View Of Binary Tree
You have been given a Binary Tree of integers.
Your task is to print the Right view of it.
The right view of a Binary Tree is a set of nodes visible when the tree is viewed from the Right side and the nodes are printed from top to bottom order.

Input Format
The only line of input contains the elements of the tree in the level order form separated by a single space.
If any node does not have left or right child, take -1 in its place. Refer to the example below.
  
Constraints
Time:- 1 Sec

Output Format
Output for every test case will be in a separate line.

Sample Input 0
2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 0
2 10 2

Sample Input 1
1 2 -1 3 -1 4 -1 5 -1 -1 -1

Sample Output 1
1 2 3 4 5

Python Code:

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while i < len(nodes):
        current_node = queue.pop(0)
        if nodes[i] != -1:
            current_node.left = TreeNode(int(nodes[i]))
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] != -1:
            current_node.right = TreeNode(int(nodes[i]))
            queue.append(current_node.right)
        i += 1
    return root
def right_view(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop(0)
            if i == level_size - 1:
                result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return result
input_str = input().strip().split()
nodes = [int(val) if val != '-1' else -1 for val in input_str]
root = build_tree(nodes)
result = right_view(root)
print(" ".join(map(str, result)))
