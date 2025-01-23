# Breadth-First Search (BFS) in Python

## Overview

Breadth-First Search (BFS) is a graph traversal algorithm that explores all the vertices of a graph level by level, starting from a given node.

This document explains how the BFS function works in Python step by step, with code and detailed explanations.

---

## BFS Implementation

```python
from collections import deque, defaultdict

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # Initialize visited array
        visited = [0] * V
        visited[0] = 1

        # Initialize the queue and BFS result list
        queue = deque()
        queue.append(0)
        bfs = []

        # Iterate while the queue is not empty
        while queue:
            # Get the front element of the queue
            node = queue.popleft()
            bfs.append(node)

            # Traverse all its neighbors
            for neighbor in adj[node]:
                # If the neighbor is not visited, mark it and enqueue it
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)

        return bfs

# Function to add an edge to the graph
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Function to print the BFS result
def printAns(ans):
    for val in ans:
        print(val, end=" ")

if __name__ == "__main__":
    # Create an adjacency list for the graph
    adj = defaultdict(list)

    # Add edges to the graph
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

    # Create the Solution object and perform BFS
    solution = Solution()
    ans = solution.bfsOfGraph(5, adj)

    # Print the BFS result
    printAns(ans)
```

## BFS Function Code

```python
from collections import deque

def bfsOfGraph(self, V, adj):
    # Step 1: Initialize visited array
    visited = [0] * V
    visited[0] = 1

    # Step 2: Initialize the queue and BFS result list
    queue = deque()
    queue.append(0)
    bfs = []

    # Step 3: Iterate while the queue is not empty
    while queue:
        # Step 4: Dequeue a node and add it to the result
        node = queue.popleft()
        bfs.append(node)

        # Step 5: Traverse all its neighbors
        for neighbor in adj[node]:
            # Step 6: If the neighbor is not visited
            if not visited[neighbor]:
                # Step 7: Mark the neighbor as visited and enqueue it
                visited[neighbor] = 1
                queue.append(neighbor)

    # Step 8: Return the BFS result
    return bfs
```

---

## Step-by-Step Explanation

### **1. Initialize the `visited` array**

```python
visited = [0] * V
visited[0] = 1
```

- The `visited` array keeps track of which nodes have already been visited.
- It is initialized to `[0, 0, ..., 0]` (all nodes unvisited).
- The starting node `0` is marked as visited: `visited[0] = 1`.

### **2. Initialize the queue and BFS result list**

```python
queue = deque()
queue.append(0)
bfs = []
```

- **Queue**: A `deque` is used to process nodes in a **first-in-first-out (FIFO)** manner.
  - The starting node `0` is added to the queue: `queue = [0]`.
- **BFS Result List (`bfs`)**: This list will store the nodes in the order they are visited.

### **3. Iterate while the queue is not empty**

```python
while queue:
```

- The loop continues until all reachable nodes are processed and the queue becomes empty.

### **4. Dequeue a node and add it to the result**

```python
node = queue.popleft()
bfs.append(node)
```

- The front element of the queue is removed using `popleft()` and stored in `node`.
- The dequeued `node` is added to the BFS result list `bfs`.

### **5. Traverse all its neighbors**

```python
for neighbor in adj[node]:
```

- The adjacency list `adj[node]` contains all the neighbors of the current node.
- The `for` loop iterates through each neighbor of the current node.

### **6. Check if the neighbor has been visited**

```python
if not visited[neighbor]:
```

- If the neighbor has not been visited (`visited[neighbor] == 0`), proceed to the next step.

### **7. Mark the neighbor as visited and enqueue it**

```python
visited[neighbor] = 1
queue.append(neighbor)
```

- Mark the neighbor as visited to ensure it is not processed again.
- Add the neighbor to the queue so it will be processed in subsequent iterations.

### **8. Return the BFS result**

```python
return bfs
```

- After the queue is empty, all reachable nodes have been visited, and the BFS traversal is complete. The function returns the `bfs` list containing the order of visited nodes.

---

## Example Walkthrough

### Graph Representation:

The graph is represented using an adjacency list:

```
0: [1, 4]
1: [0, 2, 3]
2: [1]
3: [1]
4: [0]
```

### Step-by-Step Execution:

1. **Initialization**:

   - `visited = [1, 0, 0, 0, 0]` (starting node 0 is marked visited).
   - `queue = [0]` (starting node is enqueued).
   - `bfs = []` (result list is empty).

2. **Iteration 1**:

   - `node = 0` (dequeue `0` from the queue).
   - `bfs = [0]` (add `0` to the result list).
   - Neighbors of `0`: `[1, 4]`.
     - Mark `1` as visited, enqueue it: `visited = [1, 1, 0, 0, 0]`, `queue = [1]`.
     - Mark `4` as visited, enqueue it: `visited = [1, 1, 0, 0, 1]`, `queue = [1, 4]`.

3. **Iteration 2**:

   - `node = 1` (dequeue `1` from the queue).
   - `bfs = [0, 1]` (add `1` to the result list).
   - Neighbors of `1`: `[0, 2, 3]`.
     - `0` is already visited (skip it).
     - Mark `2` as visited, enqueue it: `visited = [1, 1, 1, 0, 1]`, `queue = [4, 2]`.
     - Mark `3` as visited, enqueue it: `visited = [1, 1, 1, 1, 1]`, `queue = [4, 2, 3]`.

4. **Iteration 3**:

   - `node = 4` (dequeue `4` from the queue).
   - `bfs = [0, 1, 4]` (add `4` to the result list).
   - Neighbors of `4`: `[0]`.
     - `0` is already visited (skip it).

5. **Iteration 4**:

   - `node = 2` (dequeue `2` from the queue).
   - `bfs = [0, 1, 4, 2]` (add `2` to the result list).
   - Neighbors of `2`: `[1]`.
     - `1` is already visited (skip it).

6. **Iteration 5**:

   - `node = 3` (dequeue `3` from the queue).
   - `bfs = [0, 1, 4, 2, 3]` (add `3` to the result list).
   - Neighbors of `3`: `[1]`.
     - `1` is already visited (skip it).

7. **Queue is Empty**:
   - Exit the loop and return the result: `bfs = [0, 1, 4, 2, 3]`.

---

## Final Output

The BFS traversal of the graph starting from node `0` is:

```
0 1 4 2 3
```

The line adj = defaultdict(list) creates an adjacency list for the graph using Python’s collections.defaultdict.

What is an adjacency list?

An adjacency list is a way to represent a graph where each vertex (node) stores a list of its connected neighbors. For example:
• A graph with edges ￼ will be represented as:

0: [1, 4]
1: [0, 2, 3]
2: [1]
3: [1]
4: [0]

## Why use `defaultdict`?

The `defaultdict` simplifies working with dictionaries where missing keys need a default value.

### What is `defaultdict`?

- It’s a subclass of Python’s built-in `dict`.
- If a key that doesn’t exist is accessed, it automatically initializes the key with a default value (determined by the function passed to `defaultdict`).

In this case:

- `defaultdict(list)` automatically initializes any new key with an empty list (`[]`).
- This is particularly useful for an adjacency list, where we can directly append neighbors to the list without first checking if the key exists.

### Without `defaultdict`:

```python
adj = {}  # Normal dictionary
if 0 not in adj:
    adj[0] = []  # Initialize key 0 with an empty list
adj[0].append(1)
```

### With `defaultdict`:

```python
from collections import defaultdict

adj = defaultdict(list)  # Automatically initializes missing keys with an empty list
adj[0].append(1)  # No need to check if the key exists
```

### How does it work here?

In the context of a graph:

- `adj` is used to represent the adjacency list of the graph.
- When you add an edge between two nodes (e.g., `addEdge(adj, 0, 1)`), the function appends `1` to `adj[0]` and `0` to `adj[1]`.
- If `0` or `1` are not already keys in `adj`, they are automatically created with an empty list as their value.

This makes it easy and efficient to build the adjacency list without extra checks or initialization.

### Detailed Explanation of `addEdge`:

The function:

```python
def addEdge(adj, u, v):
    adj[u].append(v)  # Add v to the adjacency list of u
    adj[v].append(u)  # Add u to the adjacency list of v (since the graph is undirected)
```

- `adj[u].append(v)`: Adds node `v` to the list of neighbors for node `u`.
- `adj[v].append(u)`: Adds node `u` to the list of neighbors for node `v` (because it’s an undirected graph).

### Example Breakdown of Each Line:

```python
addEdge(adj, 0, 1)
```

- This adds an edge between nodes `0` and `1`.
- After this line, the adjacency list (`adj`) looks like:

```
0: [1]
1: [0]
```

```python
addEdge(adj, 1, 2)
```

- This adds an edge between nodes `1` and `2`.
- The updated adjacency list becomes:

```
0: [1]
1: [0, 2]
2: [1]
```

```python
addEdge(adj, 1, 3)
```

- This adds an edge between nodes `1` and `3`.
- The adjacency list becomes:

```
0: [1]
1: [0, 2, 3]
2: [1]
3: [1]
```

```python
addEdge(adj, 0, 4)
```

- This adds an edge between nodes `0` and `4`.
- The final adjacency list becomes:

```
0: [1, 4]
1: [0, 2, 3]
2: [1]
3: [1]
4: [0]
```

### Resulting Graph:

The graph represented by the adjacency list looks like this:

```
    0
   / \
  1   4
 / \
2   3
```

### Why This Step is Important:

The lines:

```python
addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)
addEdge(adj, 0, 4)
```

are defining the structure of the graph. Without these, the graph would be empty, and the BFS traversal would not have any connections to explore.
