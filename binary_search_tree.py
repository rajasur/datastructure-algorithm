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

root=BST(10)
l=[6,3,1,6,98,3,7]
for i in l:
    root.insert(i) 
root.preorder()
print()
root.in_order()
print()
root.post_order()