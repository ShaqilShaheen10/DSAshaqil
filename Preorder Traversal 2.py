Preorder Traversal 2
You are given the root node of a binary tree.Print its preorder traversal.

Input Format
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication 
whether the left or right node data exist for root, it will not be a part of the node data.

Constraints
1 <= N <= 10^6
Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Output Format
The only line of output prints the preorder traversal of the given binary tree.

Sample Input 0
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1

Sample Output 0
1 2 4 5 3 6 7

Sample Input 1
5 -1 -1

Sample Output 1
5

Python Code:

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def preorder_traversal(root):
    result = []
    if root:
        result.append(root.value)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result
def build_binary_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    current_index = 1
    while queue:
        current_node = queue.pop(0)
        if current_index < len(nodes) and nodes[current_index] != '-1':
            current_node.left = TreeNode(int(nodes[current_index]))
            queue.append(current_node.left)
        current_index += 1
        if current_index < len(nodes) and nodes[current_index] != '-1':
            current_node.right = TreeNode(int(nodes[current_index]))
            queue.append(current_node.right)
        current_index += 1
    return root
node_data = input().split()
root_node = build_binary_tree(node_data)
result = preorder_traversal(root_node)
print(" ".join(map(str, result)))
