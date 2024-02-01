Diameter of Binary tree
Given Binary tree Please find the diamater of that tree

Input Format
The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left 
or right node data exist for root, it will not be a part of the node data.

Constraints
Time:- 1 Sec

Output Format
The only line of output prints an integer, representing the diameter of the tree.

Sample Input 0
2 4 5 6 -1 -1 7 20 30 80 90 -1 -1 8 -1 -1 9 -1 -1 -1 -1 -1 -1
  
Sample Output 0
8
  
Sample Input 1
1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
  
Sample Output 1
4

Python Code:

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def height_and_diameter(root):
    if root is None:
        return 0, 0
    left_height, left_diameter = height_and_diameter(root.left)
    right_height, right_diameter = height_and_diameter(root.right)
    current_diameter = left_height + right_height + 1
    current_height = max(left_height, right_height) + 1
    return current_height, max(left_diameter, right_diameter, current_diameter)
def build_tree(data):
    root = Node(data[0])
    queue = [root]
    i = 1
    while i < len(data):
        current = queue.pop(0)
        if data[i] != -1:
            current.left = Node(data[i])
            queue.append(current.left)
        i += 1
        if i < len(data) and data[i] != -1:
            current.right = Node(data[i])
            queue.append(current.right)
        i += 1
    return root
input_data = input().strip()
tree_data = list(map(int, input_data.split()))
root = build_tree(tree_data)
height, diameter = height_and_diameter(root)
print(diameter-1)
