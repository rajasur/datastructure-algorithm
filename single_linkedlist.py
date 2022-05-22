#Implementation Of Single LinkedList using Python

#Create Node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
#create LinkedList
class LinkedList:
    #create head Node in LinkedList
    def __init__(self):
        self.head=None
        
    #Traversal of LinkedList
    def Traversal(self):
        if self.head is None:
            print("LinkedList is Empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
                
#Insertion at the begining                
    def add_atbegin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
 #Insertion at the  end postion       
    def add_atEnd(self,data):
        #If LinkedList is empty
        new_node=Node(data)
        if self.head is None:
            self.head=new_node 
        #If Linkedlist is not empty
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref 
            n.ref=new_node
            
 #Insert the Value Inbetween i.e add at After
    def add_atAfter(self,dat,val):
        n=self.head 
        while n is not None:
            if dat==n.data:
                break 
            else:
                n=n.ref 
        if n is None:
            print("Data is not found in LinkedList")
        else:
            new_node=Node(val)
            new_node.ref=n.ref
            n.ref=new_node
            
 #Insert the value Inbetween i.e add at Before
    def add_atBefore(self,dat,val):
        if self.head==None:
            print("LinkedList is Empty!!")
            return
        if self.head.data==dat:
            new_node=Node(val)
            new_node.ref=self.head 
            self.head=new_node
            return
        n=self.head 
        while n is not None:
            if n.ref.data==dat:
                break 
            else:
                n=n.ref 
        if n is None:
            print("Data is not found in the LinkedList")
        else:
            new_node=Node(val)
            new_node.ref=n.ref
            n.ref=new_node
            
 #Delete the Node from Begining of the LinkedList            
    def deleteAtBegin(self):
        if self.head is None:
            print("LinkedList is Empty!!")    
        else:
            self.head=self.head.ref
 
 #Delete the Node from end of the LinkedList           
    def deleteAtLast(self):
        if self.head is None:
            print("LinkedList is Empty")
            
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref  
            n.ref=None
 
#Delete the Node by giving any Value      
    def deleteByValue(self,val):
        if self.head is None:
            print("LinkedList is Empty!")
            return
        if val==self.head.data:
            self.head=self.head.ref 
            return
        n=self.head
        while n.ref is not None:
            if val==n.ref.data:
                break 
            n=n.ref 
        if n.ref is None:
            print("Node is not found in the LinkedList")
        else:
            n.ref=n.ref.ref         
 
    
                
                
        
        
#Menu Driven Program
LL=LinkedList()
while(True):
    print("\nInsert at Begin Press 1\n")
    print("\nInsert at end Press 2\n")
    print("\nInsert at after Press 3\n")
    print("\nInsert at before Press 4\n")
    print("\nDelete at Begin Press 5\n")
    print("\nDelete at End Press 6\n")
    print("\nDelete by value press 7\n")
    print("Traverse LinkedList press 8\n")
    print("Exit from the operation press 9")
    num=int(input())
    if num==1:
        val=int(input("Enter the value that you want to add at begining: "))
        LL.add_atbegin(val)
        
    if num==2:
        val=int(input("Enter the value that you want to add at end: "))
        LL.add_atEnd(val)
        
    if num==3:
        dat=int(input("Enter the value where you want to insert it: "))
        val=int(input("Enter the value that you want to add at After: "))
        LL.add_atAfter(dat,val)
        
    if num==4:
        dat=int(input("Enter the value where you want to insert it: "))
        val=int(input("Enter the value that you want to add at Before: "))
        LL.add_atBefore(dat,val)
        
    if num==5:
        LL.deleteAtBegin()
        
    if num==6:
        LL.deleteAtLast()
        
    if num==7:
        val=int(input("Enter the value that you want to delete: "))
        LL.deleteByValue(val)
        
    if num==8:
        LL.Traversal()
        
    if num==9:
        exit()