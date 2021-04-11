#construct completely balanced tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):

    if root is None:                    #if root is empty
        root = BinaryTreeNode(newValue)
        return root

    if newValue < root.data:                        #left subtree
        root.leftChild = insert(root.leftChild, newValue)
    else:

        root.rightChild = insert(root.rightChild, newValue)        #right subtree
    return root


def height(root):

    if root == None:              #if empty tree
        return 0

    hleft = height(root.leftChild)        #height of lst
    hright = height(root.rightChild)      #height of rst

    if hleft > hright:                    #compare both heights
        return hleft + 1
    else:
        return hright + 1


def CheckBalancedBinaryTree(root):
    # if tree is empty,return True
    if root == None:
        return True

    lheight = height(root.leftChild)
    rheight = height(root.rightChild)

    if (abs(lheight - rheight) > 1):
        return False
    lcheck = CheckBalancedBinaryTree(root.leftChild)   #if lst is balanced
    rcheck = CheckBalancedBinaryTree(root.rightChild)  #if rst is balanced

    if lcheck == True and rcheck == True:   #if lst and rst are equal
        return True


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
insert(root,5)
insert(root,8)

print(CheckBalancedBinaryTree(root))
