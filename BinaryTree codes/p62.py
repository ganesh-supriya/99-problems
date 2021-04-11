class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def countnode(root):
        if(root==None or (root.left==None and root.right==None)):
            return 0
        return (1+countnode(root.left)+countnode(root.right))

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print(countnode(root))