#construct completely balanced binary tree
class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key>data:                 #left child part
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=bst(data)      #creating new obj means creating new node
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=bst(data)
def height(root):
        if root==None:
            return 0
        hleft=height(root.lchild)
        hright=height(root.rchild)

        if hleft>hright:
            return hleft+1
        else:
            return hright+1
root=insert(6,15)
insert(root,10)
insert(root,25)


#error