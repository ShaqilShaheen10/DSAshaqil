Print the reverse of a Linked List
You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.

Input Format
The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.

Constraints
0 <= M <= 10^3
Time Limit: 1sec
Where 'M' is the size of the singly linked list.

Output Format
Reversed LinkedList
  
Sample Input 0
1 2 3 4 5 -1
  
Sample Output 0
5 4 3 2 1
  
Sample Input 1
5 4 3 2 1 -1
  
Sample Output 1
1 2 3 4 5

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def print_reverse(head):
    if not head:
        return
    reversed_list = []
    current = head
    while current:
        reversed_list.append(current.data)
        current = current.next
    for item in reversed_list[::-1]:
        print(item, end=" ")
def create_linked_list(input_str):
    elements = list(map(int, input_str.split()))
    head = None
    current = None
    for element in elements:
        if element == -1:
            break
        new_node = Node(element)
        if not head:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node
    return head
input_str = input()
head = create_linked_list(input_str)
print_reverse(head)
