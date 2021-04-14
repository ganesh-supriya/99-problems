#graph path

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


class Graph:

    def __init__(self, edges, N):

        self.adj = [[] for _ in range(N)]


        for current in edges:

            self.adj[current.src].append(current.dest)

def printGraph(graph):
    for src in range(len(graph.adj)):

        for dest in graph.adj[src]:
            print(f"({src} —> {dest}) ", end="")
        print()


edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),
             Edge(3, 2), Edge(4, 5), Edge(5, 4)]

N = 6
graph = Graph(edges, N)
printGraph(graph)


