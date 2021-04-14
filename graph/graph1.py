#sample graph
class graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                pass
            else:
                self.graph_dict[start]=[end]
        print("graph dict:",self.graph_dict)

routes=[
    ('mumbali','paris'),
    ('mumbai','dubai'),
    ('paris','dubai'),
    ('paris','new-york'),
    ('dubai','new-york'),
    ]

routes_graph=graph(routes)