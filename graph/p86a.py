class graph:
    v=None
    e=None
    direc=[]

    def __init__(self,v,e):
        self.v=v
        self.e=e
        self.direc=[[0 for i in range(v)]
                    for j in range(v)]

def creategraph(v,e):
    g = graph(v,e)
    g.direc[0][1]=1
    g.direc[0][2] = 1
    g.direc[0][3] = 1

    g.direc[1][0]=1
    g.direc[1][3] = 1

    g.direc[2][0] = 1
    g.direc[2][3] = 1

    g.direc[3][0] = 1
    g.direc[3][1] = 1
    g.direc[3][2] = 1

    return g

def find_degree(g,ver):
    degree=0
    for i in range(g.v):
        if g.direc[ver][i]==1:
            degree+=1
    if g.direc[ver][ver]==1:
        degree+=1
    return degree

vertices=4
edges=5
g=creategraph(vertices,edges)
ver=0
print(find_degree(g,ver))
