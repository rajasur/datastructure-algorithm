class BST:
    def __init__(self,key):
        self.key=key 
        self.lchild=None
        self.rchild=None 
    
    #Insertion of Node in BST  
    def insert(self,data):
        if self.key is None:
            self.key=data 
            return 
        if self.key==data:
            return 
        if self.key>data:
            if self.lchild is None:
                self.lchild=BST(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild=BST(data)
            else:
                self.rchild.insert(data)
                
    #Traversal of BST 
    #1. Preorder Traversal
    def preorder(self):
        if self.key:
            print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
            
    #2. Inorder Traversal
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        if self.key:
            print(self.key,end=" ")
        if self.rchild:
            self.rchild.in_order()
    #3. Postorder Traversal
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        if self.key:
            print(self.key,end=" ")
            
    #Searching the value in BST
    def search(self,data):
        if self.key==data:
            print("Data is found in the BST")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data is not found")
        if self.key<data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Data is not found.")
                
    #Deletion operation in BST
    def delete(self,data):
        if self.key is None:
            print("Tree is empty!!")
            return 
        if self.key < data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Tree is empty!!")
        elif self.key > data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Tree is Empty!!")
        else:
            #If O node is present in the both side
            if self.lchild is None:
                temp=self.rchild 
                self=None 
                return temp
            #If 1 node is present in the both side
            if self.rchild is None:
                temp=self.lchild 
                self=None 
                return temp
            #If both node is present in the both side 
            node=self.rchild
            while node.lchild:
                node = node.lchild
            self.key=node.key 
            self.rchild=self.rchild.delete(node.key)
        return self

root=BST(10)
l=[6,3,1,6,98,3,7]
for i in l:
    root.insert(i) 
root.preorder()
print()
root.in_order()
print()
root.post_order()
print()
root.search(10)
print("Before Deleting")
root.delete(6)
print("After deleting")
root.preorder()