Maximum Element in LinkedList
You are given a Linked List and you need to find the largest or maximum element that is present in the LinkedList

Input Format
First and the only line of each test case or query contains elements of the singly linked list separated by a single space.

Constraints
0 <= N <= 10^5
Time Limit: 1 sec

Output Format
Maximum or Largest Element present in the Linked List

Sample Input 0
1 2 3 4 5 -1

Sample Output 0
5

Sample Input 1
10 20 30 40 50 -1

Sample Output 1
50

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def find_maximum_element(head):
    if head is None:
        return None
    max_element = head.data
    current = head.next
    while current is not None:
        max_element = max(max_element, current.data)
        current = current.next
    return max_element
if __name__ == "__main__":
    elements = list(map(int, input().split()))
    head = None
    tail = None
    for element in elements:
        if element == -1:
            break
        new_node = Node(element)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    max_element = find_maximum_element(head)
    print(max_element)
