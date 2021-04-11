#print all leafs of tree
class node:

  def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

  def insert(self,data):
    if self.data:
        if data<self.data:
            if self.left is None:
                self.left=node(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            if self.right is None:
                self.right=node(data)
            else:
                self.right.insert(data)
    else:
        self.data=data
  def leafcount(self):
    cnt=0
    if self.left:
        cnt+=1
    if self.right:
        cnt+=1
    return cnt

  def leafcollect(self):
    if self.leafcount()==0:
        print(self.data)
        return

    if self.left:
        self.left.leafcollect()
    if self.right:
        self.right.leafcollect()

tree=node(5)
tree.insert(8)
tree.insert(7)
tree.insert(6)
tree.insert(3)
tree.insert(2)
tree.insert(11)
tree.insert(9)
tree.insert(4)
tree.leafcollect()

