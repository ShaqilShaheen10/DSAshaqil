Check If Binary Tree is BST or not
Given a binary tree with N number of nodes, check if that input tree is BST (Binary Search Tree). If yes, return true, return false otherwise.
Note: Duplicate elements should be kept in the right subtree.
Input Format

The first line of input contains data of the nodes of the tree in level order form. The data of the nodes of the tree is separated by space.
If any node does not have a left or right child, take -1 in its place. Since -1 is used as an indication whether the left or right nodes exist, 
therefore, it will not be a part of the data of any node.
  
Constraints
Time:- 1 Sec

Output Format
The first and only line of output contains either true or false.
  
Sample Input 0
3 1 5 -1 2 -1 -1 -1 -1
  
Sample Output 0
true
  
Sample Input 1
5 2 10 0 1 -1 15 -1 -1 -1 -1 -1 -1
  
Sample Output 1
false

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def isBSTUtil(root, min_val=-float('inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.data <= min_val or root.data > max_val:
        return False
    return isBSTUtil(root.left, min_val, root.data) and isBSTUtil(root.right, root.data, max_val)
def isBST(root):
    return isBSTUtil(root)
def buildTree(arr):
    if arr[0] == -1:
        return None
    root = Node(arr[0])
    queue = [root]
    i = 1
    while i < len(arr) and queue:
        node = queue.pop(0)
        node.left = Node(arr[i]) if arr[i] != -1 else None
        node.right = Node(arr[i+1]) if arr[i+1] != -1 else None
        queue.append(node.left) if node.left else None
        queue.append(node.right) if node.right else None
        i += 2
    return root
input_arr = list(map(int, input().split()))
root = buildTree(input_arr)
if isBST(root):
    print("true")
else:
    print("false")
