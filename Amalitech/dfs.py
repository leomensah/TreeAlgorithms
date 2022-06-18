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


nodes = ["A", "B", "C", "D", "E"]
all_edges = [
    ("A", "B"),
    ("A", "C"), ("B", "D"), ("C", "D"), ("C","E"), ("D", "E")
]
graph = Graph(nodes, directed=False)
for elem in all_edges:
    graph.add_edge(elem[0], elem[1])

print(graph.print_adj_list())

def DFS(graph, source, visited=None, path=None):
    if not visited:
        visited = set()
    if not path:
        path = []
    visited.add(source)
    path.append(source)

    print(source, end=' ')
    for neighbour in graph.adj_list[source]:
        if neighbour not in visited:
            DFS(graph, neighbour, visited, path)
    return path

DFS(graph, "A")

