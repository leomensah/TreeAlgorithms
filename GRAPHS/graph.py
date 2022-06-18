num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

print(num_nodes, len(edges))
# print(len(edges))

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def add_edge(self, vertex1, vertex2):
        self.data[vertex1].append(vertex2)
        self.data[vertex2].append(vertex1)

    def __repr__(self):
        return "\n".join([f"{n}: {neighbors}"for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

    def addEdge(self, edge):
        pass

# The Breadth First Search Algorithm
def bfs(graph, root):
    queue = []
    distance = [None] * len(graph.data)
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)

    visited[root] = True
    distance[root] = 0
    queue.append(root)

    idx = 0
    while idx < len(queue):
        # Deque Operation
        current = queue[idx]
        idx += 1

        # Check all edges of current
        for node in graph.data[current]:
            if not visited[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                visited[node] = True
                queue.append(node)

    return queue, distance, parent

def dfs(graph, source):
    stack = []
    visited = [False] * len(graph.data)
    result = []
    stack.append(source)
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not visited[node]:
                    stack.append(node)
    return result 


#1. Write a function to add an edge to the nodes in the graph
#2. Write a function to remove an edge from the list 
    
graph1 = Graph(num_nodes, edges)
print(dfs(graph1, 3))