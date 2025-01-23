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