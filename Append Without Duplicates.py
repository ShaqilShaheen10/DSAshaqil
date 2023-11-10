Append Without Duplicates
Given an unsorted list of nodes. The task is to remove duplicates from the list.

Input Format
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Constraints
Time Limit: 1sec

Output Format
For each test case/query, print the resulting singly linked list of integers in a row, separated by a single space.
                                                                                                      
Sample Input 0
1 2 3 1 2 -1
                                                                                                      
Sample Output 0
1 2 3
                                                                                                      
Sample Input 1
2 3 4 -1
                                                                                                      
Sample Output 1
2 3 4

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_duplicates(head):
    if not head or not head.next:
        return head
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head
def print_linked_list(head):
    while head:
        if head.data != -1:
            print(head.data, end=" ")
        head = head.next
    print()
def create_linked_list(elements):
    if not elements or elements[0] == -1:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head
input_str = input()
input_list = list(map(int, input_str.split()))
head = create_linked_list(input_list)
result = remove_duplicates(head)
print_linked_list(result)
