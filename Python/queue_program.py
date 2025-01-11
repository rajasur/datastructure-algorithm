class Queue:
    def __init__(self):
        self.queue=[] 
    
    def is_empty(self):
        return self.queue==[]
        
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None
        
    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue

def main():
    q=Queue()
    while True:
        print("\nMenu")
        print("1.Enque, 2.Dequeue, 3.Peek, 4.Size, 5.display, 6.exit")
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            data=int(input("Enter your data: "))
            q.enqueue(data)
        elif choice==2:
            res=q.dequeue()
            if res:
                print(f"dequeue eliment is {res}")
        elif choice==3:
            res=q.peek()
            if res:
                print(f"pick element is {res}")
        elif choice==4:
            res=q.size()
            if res:
                print(f"size of queue is {res}")
        elif choice==5:
            res=q.display()
            print(res)
        elif choice==6:
            break 
        else:
            print("Invalid entry")
            
if __name__== "__main__":
    main()