# Represents the node of a list
class Node:
    def __init__(self, data):
        self.data = data #data attribute stores the value of the node
        self.next = None #next attribute points to the next node in the list

class CreateList: #It is created to manage the circular linked list
    # Declaring head and tail pointers as null
    def __init__(self):
        self.head = None
        self.tail = None

    # This function will add a new node at the end of the list
    def add(self, data):#add method adds new nodes to the list
        newNode = Node(data)# Creating data as input and create a new node instance with the given data
        
        # Check if the list is empty
        if self.head is None:
            # If the list is empty, both head and tail would point to the new node
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # Tail will point to the new node
            self.tail.next = newNode
            # New node will become the new tail
            self.tail = newNode
            # Since it is a circular linked list, tail will point to head
            self.tail.next = self.head

    # Displays all the nodes in the list
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the circular linked list:")

        # Prints each node by incrementing the pointer
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)

# Create a circular linked list instance
c1 = CreateList()

# Add data to the list
c1.add(1)
c1.add(2)
c1.add(3)
c1.add(4)

# Display all the nodes present in the list
c1.display()



