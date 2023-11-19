Queue Using Array 1
Write a program to implement Queue using array.
  
Input Format
First Line array size
Second line array elements

Output Format
Print the elements from queue

Sample Input 0
5
1 2 3 4 5

Sample Output 0
1 2 3 4 5

Sample Input 1
3
1 2 3

Sample Output 1
1 2 3

Python Code:

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    def enqueue(self, element):
        if self.rear == self.size - 1:
            print("Queue is full. Cannot enqueue element.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = element
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty. Cannot dequeue element.")
            return None
        else:
            dequeued_element = self.queue[self.front]
            self.front += 1
            if self.front > self.rear:
                self.front = self.rear = -1
            return dequeued_element
    def print_queue(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
size = int(input())
elements = list(map(int, input().split()))
queue = Queue(size)
for element in elements:
    queue.enqueue(element)
queue.print_queue()
