Even after Odd Linked List
For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. 
The relative order of the odd and even terms should remain unchanged.

Input Format
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
                                                                                                      
Constraints
Time :- 1 sec
                                                                                                      
Output Format
Output for every test case will be printed in a seperate line.
                                                                                                      
Sample Input 0
1 4 5 2 -1
                                                                                                      
Sample Output 0
1 5 4 2
                                                                                                      
Sample Input 1
1 11 3 6 8 0 9 -1
                                                                                                      
Sample Output 1
1 11 3 9 6 8 0

Python Code:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def rearrange_odd_even(head):
    if head is None or head.next is None:
        return head
    odd_head, even_head = None, None
    odd_tail, even_tail = None, None
    current = head
    while current:
        if current.data % 2 == 1:  
            if odd_tail:
                odd_tail.next = current
                odd_tail = current
            else:
                odd_head = odd_tail = current
        else:  
            if even_tail:
                even_tail.next = current
                even_tail = current
            else:
                even_head = even_tail = current
        current = current.next
    if odd_tail:
        odd_tail.next = even_head
    if even_tail:
        even_tail.next = None
    return odd_head if odd_head else even_head
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
def create_linked_list_from_input():
    elements = list(map(int, input().split()))
    if not elements:
        return None
    if elements[-1] == -1:
        elements.pop()
    head = Node(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = Node(elem)
        current = current.next
    return head
if __name__ == "__main__":
    head_0 = create_linked_list_from_input()
    head_0 = rearrange_odd_even(head_0)
    print_linked_list(head_0)
