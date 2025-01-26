### Search

---

**1.** Check BST is empty

- If yes: print message
- No: compare root key with given value
  **2.** \*\*root == given value:
- Yes: then print key found
- No: check where to search for key{you can search in different way}
  **3.** Given value < Root key:
- Yes: Search left subtree, start from step 1
- No: Search right subtree: start from step 1

### Insertion

---

**1** Check BST is empty:

- If yes: Insert the new node
- No: compare root key with given value{you can compare in many ways}
  **2.** root key < given value:
- Yes: Then goto right subtree find the correct position of newnode insert new node
- No: Then goto left subtree find the correct position of newnode insert new node.

### Deletion

---

**Case1:** Deleting the node that has 0 children

1. Find the node to be deleted.
2. Remove the node from the tree.
3. Update the parent node to remove the reference to the deleted node.

**Case2:** Deleting the node that has 1 child node

1. Find the node to be deleted.
2. Replace the node with its child node.
3. Update the parent node to reference the child node.

**Case3:** Deleting the node that has 2 child nodes

1. Find the node to be deleted.
2. Find the in-order successor (smallest node in the right subtree) or in-order predecessor (largest node in the left subtree).
3. Replace the node's value with the in-order successor's or predecessor's value.
4. Recursively delete the in-order successor or predecessor.

### Traversal

---

**Pre-Order Traversal**:

1.  Visit the root node.
2.  Traverse the left subtree in pre-order.
3.  Traverse the right subtree in pre-order.

**Post-Order Traversal**:

1.  Traverse the left subtree in post-order.
2.  Traverse the right subtree in post-order.
3.  Visit the root node.

**In-Order Traversal**:

1.  Traverse the left subtree in in-order.
2.  Visit the root node.
3.  Traverse the right subtree in in-order.
