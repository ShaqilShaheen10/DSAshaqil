Serialize and Deserialize of Binary tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted
across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Input Format

The only line of each test case contains elements in the level order form. The line consists of values of nodes separated by a single space.
In case a node is null, we take -1 in its place. So -1 would not be a part of the tree nodes.

Constraints
Time:- 1 Sec

Output Format
Print the output of each test case in a separate line.

Sample Input 0
1 -1 3 -1 -1

Sample Output 0
1 -1 3 -1 -1 

Sample Input 1
3 4 -1 -1 -1

Sample Output 1
3 4 -1 -1 -1

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def serialize(root):
    if not root:
        return "-1"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.data))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("-1")
    return " ".join(result)
def deserialize(data):
    values = data.split()
    if not values or values[0] == "-1":
        return None
    root = Node(int(values[0]))
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        left_value = values[i]
        i += 1
        if left_value != "-1":
            node.left = Node(int(left_value))
            queue.append(node.left)
        right_value = values[i]
        i += 1
        if right_value != "-1":
            node.right = Node(int(right_value))
            queue.append(node.right)
    return root
if __name__ == "__main__":
    input_line = input().strip()
    values = list(map(int, input_line.split()))
    root = Node(values[0])
    current_level = [root]
    i = 1
    while current_level and i < len(values):
        next_level = []
        for node in current_level:
            if i < len(values) and values[i] != -1:
                node.left = Node(values[i])
                next_level.append(node.left)
            i += 1
            if i < len(values) and values[i] != -1:
                node.right = Node(values[i])
                next_level.append(node.right)
            i += 1
        current_level = next_level
    serialized_tree = serialize(root)
    print(serialized_tree)
