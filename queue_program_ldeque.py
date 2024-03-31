import collections as cs

class Queue:
    def __init__(self):
        self.queue=cs.deque()
        
    def left_insert(self,data):
        self.queue.appendleft(data)
    
    def is_empty(self):
        return self.queue==cs.deque()
        
    def right_delete(self):
        if self.is_empty():
            print("Queue is Empty!!")
        else:
            self.queue.pop()
        
    def display(self):
        print(self.queue)
        
q=Queue()
        
while True:
    print("\nMenu")
    print("1.Insert, 2.Delete, 3.Display, 4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=int(input("Enter your data: "))
        q.left_insert(data)
        
    elif choice==2:
        q.right_delete()
        
    elif choice==3:
        q.display()
        
    elif choice==4:
        break 
    else:
        print("Invalid Entry")