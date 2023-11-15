Palindrome of a Linked List
You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

Input Format
First and the only line of each test case or query contains the the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.

Constraints
0 <= M <= 10^5
Time Limit: 1sec
Where 'M' is the size of the singly linked list.
                                                                                                      
Output Format
For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
                                                                                                      
Sample Input 0
9 2 3 3 2 9 -1
                                                                                                      
Sample Output 0
true
                                                                                                      
Sample Input 1
-1
                                                                                                      
Sample Output 1
true

Python Code:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
def is_palindrome(head):
    def reverse_linked_list(node):
        prev = None
        current = node
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def compare_linked_lists(list1, list2):
        while list1 is not None and list2 is not None:
            if list1.data != list2.data:
                return "false"
            list1 = list1.next
            list2 = list2.next
        return "true"
    if head is None or head.next is None:
        return "true"
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    second_half_reversed = reverse_linked_list(slow.next)
    result = compare_linked_lists(head, second_half_reversed)
    slow.next = reverse_linked_list(second_half_reversed)
    return result
def main():
    elements = list(map(int, input().split()))
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        if element == -1:
            break
        current.next = Node(element)
        current = current.next
    result = is_palindrome(head)
    print(result)
if __name__ == "__main__":
    main()
