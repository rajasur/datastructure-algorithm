import queue

class prorityQueue:
    def __init__(self):
        self.priority_queue=queue.PriorityQueue()
        
    def isEmpty(self):
        return not self.priority_queue
    
    def insert(self,data):
        self.priority_queue.put(data)
        
    def delete(self):
        if self.isEmpty():
            print("Priority queue is Empty!!")
        else:
            self.priority_queue.get()
            
    def display(self):
        elements = list(self.priority_queue.queue)
        print(elements)

def main():
    pq=prorityQueue()
    while True:
        print("\nMenu")
        print("1.Insert, 2.Delete, 3.Display, 4.Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            data=int(input("Enter your data: "))
            pq.insert(data) 
        elif choice==2:
            pq.delete()
        elif choice==3:
            pq.display()
        elif choice==4:
            break 
        else:
            print("Invalid entry")
        
        
if __name__=="__main__":
    main()