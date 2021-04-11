#count leaves of binary tree

class node:

  def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def leafcount(node):
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else:
            return leafcount(node.left)+leafcount(node.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(1)
root.right.right=node(6)

print("leaf count is ",leafcount(root))
