#Create a Node
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doubleLinkedList:
    def __init__(self):
        self.head=None

    #Traversal Operation
    def forwardTravesal(self): #This is for forward direction Traversal
        if self.head is None:
            print('Doubly LinkedList is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                if n.next is not None:
                    print("-->",end=' ')
                n=n.next

    def backwardTraversal(self): # This is for Backward direction Traversal
        if self.head is None:
            print('Doubly Linked List is empty')
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(n.data,end=' ')
                if n.prev is not None:
                    print("<--",end=' ')
                n=n.prev

    def atBegin(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            new_node.next=n.prev
            new_node.prev=None
            n.next=Null

    #Insertion operation
    def insert_empty(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            print('Doubly linkedlist is not empty!')

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.insert_empty(data)
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
            new_node.prev=n

    def add_after(self,data,x):
        if self.head is None:
            print('Doubly Linkedlist is empty!!')
        else:
            new_node=Node(data)
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.next
            if n is None:
                print('Data is not found')
            else:
                new_node.next=n.next
                new_node.prev=n
                if n.next is not None:
                    n.next.prev=new_node
                n.next=new_node

    def add_before(self,data,x):
        if self.head is None:
            print('Doubly linkedlist empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.next
            if n is None:
                print('Doubly Linked list empty')
            else:
                new_node=Node(data)
                #Continue from here



#Menu Driven Program
DLL=doubleLinkedList()
while(True):
    print("\nInsert Empty Press 1\n")
    print("Insert at Begin 2\n")
    print("Insert at End Press 3\n")
    print("Insert at before Press 4\n")
    print("Delete at Begin Press 5\n")
    print("Delete at End Press 6\n")
    print("Delete by value press 7\n")
    print("Traverse Forward Direction press 8\n")
    print("Traverse Backward Direction press 9\n")
    print("Exit from the operation press 10")
    num=int(input())
    if num==1:
        val=int(input("Enter the value that you want to add: "))
        DLL.insert_empty(val)

    if num==2:
        val=int(input("Enter the value that you want to add at Begin: "))
        DLL.add_begin(val)

    if num==3:
        val=int(input("Enter the value that you want to add at End: "))
        DLL.add_end(val)

    if num==4:
        val=int(input("Enter the value that you want to add at after: "))
        dat=int(input("Enter the value where you want to insert it: "))
        DLL.add_after(val,dat)

    if num==5:
        val=int(input("Enter the value that you want to add at before: "))
        dat=int(input("Enter the value where you want to insert it: "))
        DLL.add_before(val,dat)

    if num==6:
        DLL.deleteAtLast()

    if num==7:
        val=int(input("Enter the value that you want to delete: "))
        DLL.deleteByValue(val)

    if num==8:
        DLL.forwardTravesal()
    if num==9:
        DLL.backwardTraversal()
    if num==10:
        exit()

