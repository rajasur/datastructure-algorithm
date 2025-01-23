### What is Tree?

---

- Tree is Non-linear data structure.
- Represents relationship between nodes.
- Collection of entities called Nodes.
- Nodes are connected by edges.

### Terminologies of Tree

---

- **Node**: A basic unit of a data structure, such as a tree or linked list.
- **Root Node**: The topmost node of a tree.
- **Edge/Link**: A connection between two nodes.
- **Parent Node/Parent**: A node that has one or more child nodes.
- **Child Node/Child**: A node that is a descendant of another node.
- **Siblings**: Nodes that share the same parent.
- **Leaf Node/Leaf/External Node/Terminal Node**: A node with no children.
- **Non-Terminal Node**: A node that has at least one child.
- **Path**: A sequence of nodes and edges connecting a node with a descendant.
- **Degree of a node**: The number of children a node has.
- **Degree of Tree**: The highest degree of a node among all the nodes in the tree.
- **Level**: The number of edges on the path from the root node to the node.
- **Height of Node**: The number of edges on the longest path from the node to a leaf.
- **Height of Tree**: The height of the root node.
- **Depth of Node**: The number of edges from the root to the node.
- **Subtree**: A tree consisting of a node and its descendants.

### Example Tree

---

```
        A
       / \
      B   C
     / \   \
    D   E   F
   /       / \
  G       H   I
```

### Explanation of Terminologies with Example

---

- **Node**: Each letter (A, B, C, D, E, F, G, H, I) represents a node.
- **Root Node**: A is the root node.
- **Edge/Link**: The connections (A-B, A-C, B-D, B-E, C-F, D-G, F-H, F-I) are edges.
- **Parent Node/Parent**: A is the parent of B and C.
- **Child Node/Child**: B and C are children of A.
- **Siblings**: B and C are siblings, D and E are siblings, H and I are siblings.
- **Leaf Node/Leaf/External Node/Terminal Node**: E, G, H, and I are leaf nodes.
- **Non-Terminal Node**: A, B, C, D, and F are non-terminal nodes.
- **Path**: A-B-D-G is a path from A to G.
- **Degree of a node**: The degree of node A is 2 (B and C), the degree of node B is 2 (D and E), the degree of node C is 1 (F), the degree of node D is 1 (G), the degree of node F is 2 (H and I).
- **Degree of Tree**: The highest degree of any node in the tree is 2.
- **Level**: Node A is at level 0, nodes B and C are at level 1, nodes D, E, and F are at level 2, nodes G, H, and I are at level 3.
- **Height of Node**: The height of node B is 2 (B-D-G), the height of node A is 3 (A-B-D-G or A-C-F-H or A-C-F-I).
- **Height of Tree**: The height of the tree is 3.
- **Depth of Node**: The depth of node G is 3 (A-B-D-G).
- **Depth of Tree**: The depth of the tree is 3.
  The depth of a tree is defined as the length of the longest path from the root node to a leaf node. In other words, it is the number of edges on the longest path from the root to a leaf. For example, if a tree has a root node and the longest path to a leaf node involves traversing three edges, then the depth of the tree is 3.

- **Subtree**: The subtree rooted at B includes nodes B, D, E, and G.

### Characteristics of Tree:

---

- A tree can contain only one root node.
- In a tree if we have N nodes then we will have N-1 edges/link.
- Every child will have only one parent but parent can have multiple child.
- Tree is a recursive data structure.

### Types of Tree data structure

---

- **General Tree**: A tree data structure where each node can have an arbitrary number of children. Unlike binary trees, there is no restriction on the number of children a node can have.

  - Example:
    ```
        A
      / | \
     B  C  D
    /|   \
    E F    G
    ```

- **Binary Tree**: A tree data structure in which each node has at most two children, referred to as the left child and the right child. This structure is the basis for more complex tree structures like binary search trees, AVL trees, and red-black trees.

  - Example:
    ```
         1
        / \
       2   3
      / \
     4   5
    ```

### Types of Binary Tree

---

- **Full Binary Tree**: Full Binary tree is a type of binary tree in which every node other than leaf nodes has 2 children.

  - Example:
    ```
          1
         / \
        2   3
       / \
      4   5
    ```

- **Complete Binary Tree**: A binary tree in which all the levels are completely filled except possibly the last level, and the last level has all keys as left as possible.

  - Example:
    ```
          1
         / \
        2   3
       / \  /
      4  5 6
    ```

- **Perfect Binary Tree**: A binary tree in which all the internal nodes have two children and all leaf nodes are at the same level.

  - Example:
    ```
          1
         / \
        2   3
       / \ / \
      4  5 6  7
    ```

- **Balanced Binary Tree**: A binary tree in which the height of the left and right subtrees of any node differ by at most one. The height can be at most log(N) where N denotes the number of nodes. For example, for N=8, log base 2 of 8 is 3, so the height of a balanced binary tree should be 3.

  - Example:
    ```
                  1
                 / \
                2   3
               / \
              4   5
    ```

- **Degenerate (or Pathological) Tree**: A tree where each parent node has only one child. This structure essentially behaves like a linked list.

  - Example:
    ```
        1
         \
          2
           \
            3
             \
              4
    ```

- **Skewed Binary Tree**: A binary tree in which all the nodes have only one child either to the left or right. It can be
