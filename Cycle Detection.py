Cycle Detection
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, 
determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

Function Description
Complete the has_cycle function in the editor below.
It has the following parameter:
SinglyLinkedListNode pointer head: a reference to the head of the list
Returns
int:  if there is a cycle or  if there is not
Note: If the list is empty,  will be null.

Input Format
The code stub reads from stdin and passes the appropriate argument to your function. The custom test cases format will not be described for this
question due to its complexity. Expand the section for the main function and review the code if you would like to figure out how to create a custom case.

Sample Input
References to each of the following linked lists are passed as arguments to your function:

Sample Inputs
  1->null
  1->2->3-|
    |-----
Sample Output
0
1
  
Explanation
The first list has no cycle, so return 0.
The second list has a cycle, so return 1.

Python Code:

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def has_cycle(head):
    if not head:
        return 0  
    tortoise = head
    hare = head
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return 1  
    return 0  
head_with_cycle = SinglyLinkedListNode(1)
head_with_cycle.next = SinglyLinkedListNode(2)
head_with_cycle.next.next = SinglyLinkedListNode(3)
head_with_cycle.next.next.next = head_with_cycle.next  
head_without_cycle = SinglyLinkedListNode(1)
head_without_cycle.next = SinglyLinkedListNode(2)
head_without_cycle.next.next = SinglyLinkedListNode(3)
print(has_cycle(head_with_cycle))  
print(has_cycle(head_without_cycle))  
