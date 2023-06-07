# Stacks in Data Structures is a linear type of data structure that 
# follows the LIFO (Last-In-First-Out) principle and allows insertion and deletion operations 
# from one end of the stack data structure, that is top

# Implementation of the stack can be done by contiguous memory which is an array, and non-contiguous memory which is a linked list.
#  Stack plays a vital role in many applications.

# there are operations that are implemented on the stack;
# 1. Push operation involves inserting new elements in the stack. Since you have only one end to insert a unique element on top of the stack, it inserts the new element at the top of the stack.
# 2.Pop operation refers to removing the element from the stack again since you have only one end to do all top of the stack. So removing an element from the top of the stack is termed pop operation
# 3.Peek operation refers to retrieving the topmost element in the stack without removing it from the collections of data elements.
# 4.IsFull function is used to check whether or not a stack is empty
# 5.IsEmpty function is used to check whether or not a stack is empty.

# we use the append() function to push an item and the pop() function to remove an item

# Applications of Stack
# There are many applications of a stack. Some of them are:
#  • Stacks are used in backtracking algorithms. 
# • They are also used to implement undo/redo functionality in a software. 
# • Stacks are also used in syntax parsing for many compilers. 
# • Stacks are also used to check proper opening and closing of parenthesis
# example
stack=["Amar","Akbar","Anthony","Doreen", "Victory","Namyenya","Brilliant and Beautiful"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)

print(stack.pop())
print (stack)



# function to check whether a stack is empty or not
def IsEmpty():
    if len(stack)==0:
        return True
    else:
        return False
print(IsEmpty()) 
   
# if S.top == null:
#     return TRUE
# return FALSE

# Bool isFull()

# {

#   if(top == maxsize)

#  return true;

# else

#  return false;

# }


# stack using linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.top = None

def traversal(s):
    temp = s.head #temporary pointer to point to head

    a = ''
    while temp != None: #iterating over stack
        a = a+str(temp.data)+'\t'
    temp = temp.next
    ''
    print(a)

def is_empty(s):
    if s.top == None:
        return True
    return False



def push(s, n):
    if is_empty(s): #empty
        s.head = n
        s.top = n
    else:
        s.top.next = n
        s.top = n

def pop(s):
    if is_empty(s):
        print("Stack Underflow")
        return -1000
    else:
        x = s.top.data
        if s.top == s.head: # only one node
            s.top = None
            s.head = None
        else:
            temp = s.head
            while temp.next != s.top: #iterating to the last element
                temp = temp.next
                temp.next = None
                del s.top
                s.top = temp
            return x


if __name__ == '__main__':
    s = Stack()
    a = Node(10)
    b = Node(20)
    c = Node(30)

    pop(s)
    push(s, a)
    push(s, b)
    push(s, c)

    traversal(s)
    pop(s)
    traversal(s)









# class Node():
#    def __init__(self, data):
#       self.data=data
#       self.next=None
    
# class Stack():
#    def __init__ (self):
#     self.head=None
#     self.top=None
#    def traversal(s):
#       # temporary pointer to point to head
#       temp=s.head  
#       a=""
#       while temp !=None:
#          a=a+str(temp.data)+"\t"
#          temp=temp.next
#       print(a) 
#    def is_empty(s):
#       if s.top ==None:
#          return True
#       return False
#    def push(s,n):
#       # empty
#       if is_empty(s):
#          s.head=n
#          s.top=n
#       else:
#          s.top.next=n
#          s.top=n  
#    def pop(s):
#       if is_empty(s):
#          print("Stack Underflow") 
#          return -1000
#       else:
#          x=s.top.data
#         #  only one node
#       if s.top ==s.head:
#         s.top = None
#         s.head = None

#       else:
#         temp=s.head
#       # iterating to the last element
#       while temp.next!=s.top:
#          temp=temp.next
#       temp.next=None   
#       temp.next=None

#       del s.top
#       s.top=temp
#       return x   
#    if __name__   == "__main__":
#          s=Stack()


#          a=Node(10)
#          b=Node(20)
#          c=Node(30) 

#          pop(s)
#          push(s,a)
#          push(s,b)
#          push(s,c)

#          traversal(s)
#          pop(s)
#          traversal(s)




