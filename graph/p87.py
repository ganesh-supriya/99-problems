from collections import defaultdict
class Graph:

    def __init__(self):


        self.graph = defaultdict(list)         #dic to store graph


    def addEdge(self, u, v):                    #add edges to graph
        self.graph[u].append(v)

    def DFS(self, v, visited):

        visited.add(v)                          #current node check
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)

    def DFS1(self, v):                       #dfs traversAL

        visited = set()

        self.DFS(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS1(2)