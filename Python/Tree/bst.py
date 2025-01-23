# Class definition for a node in a binary tree
class Node:
    # Method to initialize the node with a value
    def __init__(self, val):
        # Set the value of the node to the passed integer
        self.data = val
        # Initialize left and right pointers as None
        self.left = None
        self.right = None

# Main code block
if __name__ == "__main__":
    # Creating a new node for the root of the binary tree
    root = Node(1)
    # Creating left and right child nodes for the root node
    root.left = Node(2)
    root.right = Node(3)
    # Creating a right child node for the left child node of the root
    root.left.right = Node(5)