### Search

---

1. Check BST is empty
   - If yes: print message
   - No: compare root key with given value
2. root == given value:
   - Yes: then print key found
   - No: check where to search for key{you can search in different way}
3. Given value < Root key:
   - Yes: Search left subtree, start from step 1
   - No: Search right subtree: start from step 1

### Insertion

---

1. Check BST is empty:
   - If yes: Insert the new node
   - No: compare root key with given value{you can compare in many ways}
2. root key < given value:
   - Yes: Then goto right subtree find the correct position of newnode insert new node
   - No: Then goto left subtree find the correct position of newnode insert new node.

### Deletion

---
