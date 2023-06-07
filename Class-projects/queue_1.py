
from collections import deque

# Queue implementation in Python

# class Queue:

#     def __init__(self):
#         self.queue = []

#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)

#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)

#     # Display  the queue
#     def display(self):
#         print(self.queue)

#     def size(self):
#         return len(self.queue)


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# q.display()

# q.dequeue()

# print("After removing an element")
# q.display()



# The Queue class that implements a basic queue data structure. 
# The Queue class is initialized with a specified size. It has attributes head and tail which represent the indices of the front and rear of the queue, respectively. Q is a list that holds the elements of the queue, and size represents the maximum size of the queue.

# The is_empty method checks if the queue is empty by comparing the head and tail indices. If they are the same, it means the queue is empty and True is returned.

# The is_full method checks if the queue is full by comparing the head and tail indices. If the tail is one position behind the head, it means the queue is full and True is returned.
# The enqueue method adds an element to the queue. If the queue is full, it prints "Queue Overflow" indicating that the queue is already at its maximum capacity. Otherwise, it adds the element x to the queue at the tail index. If the tail reaches the end of the queue, 
# it wraps around to the beginning.

# The dequeue method removes and returns the element at the front of the queue. If the queue is empty, 
# it prints "Underflow" indicating that the queue is already empty. Otherwise, 
# it removes the element at the head index and updates the head index accordingly. If the head reaches the end of the queue, it wraps around to the beginning.

# The display method prints the elements of the queue starting from the head index to the tail index.
#  It uses a loop to iterate through the queue, and if the index reaches the end of the queue, 
# it wraps around to the beginning.

# In the __main__ block, an instance of the Queue class is created with a maximum size of 10. Elements 20, 30, 40, and 50 are enqueued and then displayed. Then, two elements are dequeued and the queue is displayed again. Finally, elements 60 and 70 are enqueued, and the queue is displayed once more.





class Queue:
    def __init__(self, size):
        self.head =1
        self.tail =1
        self.Q =[0]*(size)
        self.size =size
    def is_empty(self):
            if self.tail == self.head:
                return True
            return False
        
    def is_full(self):
        if self.head == self.tail+1:
            return True
        return False
    def enqueue(self, x):
        if self.is_full():
            print("Queue Overflow")

        else:
            self.Q[self.tail]=x
            if self.tail == self.size:
                self.tail =1
            else:
                self.tail = self.tail+1
    def dequeue(self):
        if self.is_empty():
            print("Underflow")
        else:
            x= self.Q[self.head]
            if self.head ==self.size:
                self.head = 1
            else:
                self.head = self.head+1
                return x

    def display(self):
        i = self.head
        while(i<self.tail):
            print(self.Q[i])
            if(i == self.size):
              i= 0
            i= i+1

if __name__ == '__main__':
    q =Queue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.display()
    print("")
    q.dequeue()
    q.dequeue()
    q.display()
    print("")
    q.enqueue(60)
    q.enqueue(70)
    q.display()




























# Enqueue(Q,x)
#    if isFull(Q)
#       Error "Queue overflow"
#    else
#      Q|Q.tail   






# class Queue:

#     def __init__(self):
#         """
#         Initializing Queue.
#         """
#         self.queue = deque()

#     def isEmpty(self) -> bool:
#         return True if len(self.queue) == 0 else False

#     def front(self) -> int:
#         return self.queue[-1]

#     def rear(self) -> int:
#         return self.queue[0]

#     def enqueue(self, x: int) -> None:
#         self.x = x
#         self.queue.append(x)       

#     def dequeue(self) -> None:
#         self.queue.popleft()