#edges of graph
#nodes of graph

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges
def find_nodes(graph):

    nodes = []
    for node in graph:
        if  graph[node]:
            nodes += node
    return nodes

print(generate_edges(graph))
print(find_nodes(graph))

