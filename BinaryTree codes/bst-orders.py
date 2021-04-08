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
    def search(self,data):
        if self.key==data:            #check if node is present or not
            print("the node is found")
            return
        if data<self.key:            #search in left sub tree
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not found")
        else:                           #search in right sub tree
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present in tree")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()                  #recursion
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

root = bst(10)

list1=[20,4,2,6,1,8,4,40]
for i in list1:
      root.insert(i)
print("searching of node:")
root.search(6)
print("pre-order")
root.preorder()
print("\nin-order")
root.inorder()
print("\npost-order")
root.postorder()