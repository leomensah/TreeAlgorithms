# Path is an edge that connects two vertex
# TYPES OF GRAPHS
#1. CYCLIC GRAPHS
#2. ACYCLIC GRAPHS --> TREE
#3. DIRECTED GRAPHS
#4. WEIGHTED GRAPHS

# PATH
# SIMPLE PATH: VERTICES DO NOT REPEAT
# CLOSED PATH: FIRST AND LAST NODE IS THE SAME
# CYCLE: FIRST NODE AND LAST NEED TO BE SAME BUT DISTINCT NODES
# CONNECTED GRAPH IS WHEN THERE IS A PATH FROM ANY NODE TO ANY OTHER NODE
# STRONGLY CONNECTED GRAPH AND WEAKLY CONNECTED GRAPHS
# DEGREE OF A NODE IS THE NUMBER OF EDGES CONNECTED TO THE NODE

# COMPLETE GRAPH

#  GRAPH REPRESENTATION USING AN ADJACENCY MATRIX
from cmath import inf
from queue import Queue
from unittest import result
class Graph:
    def __init__(self, Nodes, directed=False):
        self.nodes = Nodes
        self.adj_list = {node: [] for node in self.nodes}
        self.directed = directed

    def add_node(self, node):
        if node in self.nodes:
            print(node, "is already in the list")
        else:
            self.nodes.append(node)
            self.adj_list[node] = []
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def degree(self, node):
        return len(self.adj_list[node])

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])


nodes = ["A", "B", "C", "D", "E", "F"]
all_edges = [
    ("A", "B"),
    ("A", "C"), ("B", "D"), ("B","E"), ("C", "B"), ("C","F"), ("E", "F")
]
graph = Graph(nodes, directed=True)
# graph.print_adj_list()

for u, v in all_edges:
    graph.add_edge(u, v)

# graph.print_adj_list()
# print("Degree of C", graph.degree("C"))

# graph.add_node("F")
# graph.print_adj_list()

# graph.add_edge('F', 'D')
# graph.print_adj_list()

# BREADTH FIRST SEARCH
# REQUIREMENTS
# SOURCE NODE
# VISITED NODE
# QUEUE DATA STRUCTURE

# ALGORITHMS FOR BREADTH FIRST SEARCH
#1. POP FIRST ELEMENT OF GRAPH
#2. APPEND TO THE LIST AND SET AS VISITED

def bfs(graph, source):
    visited = {node: False for node in graph.adj_list.keys()}
    level = {node: -1 for node in graph.adj_list.keys()}
    parent = {node: None for node in graph.adj_list.keys()}
    bfs_traversal_output = []
    queue = Queue()

    visited[source] = True
    level[source] = 0
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in graph.adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)
    return bfs_traversal_output, level, parent

def dfs(adj_list, vertex, visitedSet = None, path = None):
    if visitedSet is None:
        visitedSet = set()
    if path is None:
        path = []

    visitedSet.add(vertex)
    path.append(vertex)

    if vertex in adj_list:
        for neighbor in adj_list[vertex]:
            if neighbor not in visitedSet:
                dfs(adj_list, neighbor, visitedSet, path)
    return path

# print(dfs(graph.adj_list, 'A'))

# THE GRAPH DEPTH FIRST SEARCH ALGORITHM
time = 0
def depth_first_search(adj_list, u, color=None, trav_time=None, parent=None, dfs_traversal_output=None):
    if not color:
        color = {node: "W" for node in adj_list.keys()}
    if not parent:
        parent = {node: None for node in adj_list.keys()}
    if not trav_time:
        trav_time = {node: [-1, -1] for node in adj_list.keys()}
    if not dfs_traversal_output:
        dfs_traversal_output = []

    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            depth_first_search(adj_list, v, color, trav_time, parent, dfs_traversal_output)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

    return parent, trav_time, dfs_traversal_output

# graph.print_adj_list()
# print(depth_first_search(graph.adj_list, "A"))

# ADJACENCY LIST
adj_list = {
    "A": ["B"],
    "B": ["A","D","E"],
    "C": ["F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}
# print(depth_first_search(adj_list, "A"))

# DFS USING A STACK
# def dfs_stack(graph, root):
#     stack = []
#     discovered = {node: False for node in graph.adj_list.keys()}
#     result = []
#     stack.append(root)
    

#     while len(stack) > 0:
#         current = stack.pop()
#         if not discovered[current]:
#             discovered[current] = True
#             result.append(current)
#             for node in graph.adj_list[current]:
#                 if not discovered[node]:
#                     stack.append(node)
#     return result

# print(graph.print_adj_list())
# print(dfs_stack(graph, "A"))

# DETECT A CYCLE IN A GRAPH
adj_list2 = {
    "A": ["C", "B"],
    "B": ["D"],
    "C": [],
    "D": ["A", "E"],
    "E": []
}

def depth_cycle(adj_list, u, color=None, parent=None):
    if not color:
        color = {node: "W" for node in adj_list.keys()}
    if not parent:
        parent = {node: None for node in adj_list.keys()}

    color[u] = "G"
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            depth_first_search(adj_list, v, color, parent)
    color[u] = "B"

    return False
