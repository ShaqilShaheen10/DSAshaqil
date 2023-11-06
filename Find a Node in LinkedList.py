Find a Node in LinkedList
Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of 'n' in the linked list. -1 otherwise.
Note : Assume that the Indexing for the linked list always starts from 0.

Input Format
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line of input contains a single integer depicting the value of 'n'.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
                                                                                                      
Constraints
0 <= M <= 10^5
Where M is the size of the singly linked list.
Time Limit: 1sec

Output Format
Output for every test case will be printed in a seperate line.

Sample Input 0
3 4 5 2 6 1 9 -1
100

Sample Output 0
-1
  
Sample Input 1
10 20010 30 400 600 -1
20010
  
Sample Output 1
1

Python Code:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def find_index(head, n):
    index = 0
    current = head
    while current is not None:
        if current.data == n:
            return index
        current = current.next
        index += 1
    return -1
elements = list(map(int, input().split()))
n = int(input())
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
result = find_index(head, n)
print(result)
