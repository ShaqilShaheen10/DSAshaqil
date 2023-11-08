Print LinkedList
First take a linkedList and then try to print that LinkedList

Input Format
Take LinkedList Input

Output Format
Print the LinkedList

Sample Input 0
1 2 3 4 5 -1

Sample Output 0
1 2 3 4 5

Sample Input 1
5 6 7 8 9 -1

Sample Output 1
5 6 7 8 9

Pyton Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
if __name__ == "__main__":
    elements = list(map(int, input().split()))
    linked_list = LinkedList()
    for num in elements:
        if num == -1:
            break
        linked_list.insert(num)
    linked_list.print_linked_list()
