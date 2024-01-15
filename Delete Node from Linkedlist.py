Delete Node from Linkedlist
Given a singly linked list of integers and position 'i', delete the node present at the 'i-th' position in the linked list recursively.
Note : Assume that the Indexing for the linked list always starts from 0.

Input Format
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line of input contains a single integer depicting the value of 'i'.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
                                                                                                      
Constraints
Time:- 1 sec
                                                                                                      
Output Format
Output for every test case will be printed in a seperate line.
                                                                                                      
Sample Input 0
3 4 5 2 6 1 9 -1
3
                                                                                                      
Sample Output 0
3 4 5 6 1 9

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def deleteNodeRec(head, pos):
    if head is None:
        return head
    if pos == 0:
        new_head = head.next
        del head
        return new_head
    head.next = deleteNodeRec(head.next, pos - 1)
    return head
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
elements = list(map(int, input().split()))
position = int(input())
head = Node(elements[0])
current = head
for element in elements[1:]:
    if element == -1:
        break
    current.next = Node(element)
    current = current.next
head = deleteNodeRec(head, position)
printLinkedList(head)
