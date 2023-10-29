Delete Alternate Nodes
Given a Singly Linked List of integers, delete all the alternate nodes in the list.
Example:
List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
Alternate nodes will be: 20, 40, and 60.
Hence after deleting, the list will be:
Output: 10 -> 30 -> 50 -> null

Input Format
The first and the only line of input will contain the elements of the Singly Linked List separated by a single space and terminated by -1.

Constraints
1 <= N <= 10 ^ 6.
Where N is the size of the Singly Linked List
Time Limit: 1 sec

Output Format
The only line of output will contain the updated list elements.

Sample Input 0
1 2 3 4 5 -1

Sample Output 0
1 3 5

Sample Input 1
10 20 30 40 50 60 70 -1

Sample Output 1
10 30 50 70 

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_alternate_nodes(head):
    current = head
    while current is not None and current.next is not None:
        current.next = current.next.next
        current = current.next
    return head
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()
elements = list(map(int, input().strip().split()))
head = Node(elements[0])
current = head
for element in elements[1:]:
    if element == -1:
        break
    new_node = Node(element)
    current.next = new_node
    current = new_node
head = delete_alternate_nodes(head)
print_linked_list(head)
