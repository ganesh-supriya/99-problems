#symmetric binary tree
class newnode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def issymetric(root):
    if (root==None):
        return True
    if(not root.left and not root.right):
        return True
    q=[]

    q.append(root)
    q.append(root)

    lnode=0
    rnode=0

    while(not len(q)):
        lnode=q[0]
        q.pop(0)
        rnode=q[0]
        q.pop(0)

        if(lnode.left or rnode.right):
            q.append(lnode.left)
            q.append(rnode.right)
        elif(lnode.left or rnode.right):
            return False

        if(lnode.right and rnode.left):
            q.append(lnode.right)
            q.append(rnode.left)

        elif(lnode.right or rnode.left):
            return False
    return True

root=newnode(1)
root.left=newnode(2)
root.right=newnode(2)
root.left.left=newnode(3)
root.left.right=newnode(4)
root.right.left=newnode(4)
root.right.right=newnode(3)


if(issymetric(root)):
    print("symetric tree")
else:
    print("asymmetric root")