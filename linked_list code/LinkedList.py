class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
     def __init__(self):                          #creating head
         self.head=None

     def print_LL(self):
         if self.head is None:                     #checking if LL is empty or not...if head is empty,LL is empty.
             print("linkedlist is empty")
         else:
             n=self.head
             while n is not None:
                 print(n.data,"----->",end="")
                 n=n.ref
     def node_begin(self,data):                        #adding node at begining
          new_node=node(data)
          new_node.ref=self.head
          self.head=new_node

     def node_end(self,data):                          #adding node at the end
         new_node=node(data)
         if self.head is  None:
             self.head=new_node
         else:
             n=self.head
             while n.ref is not None:
                n = n.ref
             n.ref=new_node

     def node_after(self,data,x):
         n=self.head
         while n is not None:
             if x==n.data:
                 break
             n=n.ref
         if n is None:
             print("the node is not present in linked list")
         else:
             new_node=node(data)
             new_node.ref=n.ref
             n.ref=new_node

     def node_before(self,data,x):
        if self.head is None:
            print("the linked list is empty")
            return
        if self.head.data==x:                   #adding node before 1st node
            new_node=node(data)
            new_node.ref=self.head
            self.head=new_node
            return

        n=self.head                             #adding node at rest position
        while n.ref is not None:
           if n.ref.data==x:                    #x for the data of next node...if value match then we're on previous node
                  break
           n=n.ref
           if n.ref is None:
               print("node is not found")
           else:                                #adding node after previous node
               new_node=node(data)
               new_node.ref= n.ref
               n.ref=new_node
     def delete_by_value(self,x):                          #deleting node by value
         if self.head is None:
             print("we can't delete element because of empty linkedlist")
             return
         if x==self.head.data:
             self.head=self.head.ref
             return
         n=self.head
         while n.ref is not None:
             if x==n.ref.data:
                 break
             n=n.ref
         if n.ref is None:
             print("node is not present")
         else:
             n.ref=n.ref.ref

LL1 = linkedlist()
LL1.node_begin(10)
LL1.node_begin(20)
LL1.node_end(100)
LL1.node_begin(30)
LL1.node_before(50,20)
LL1.node_after(60,20)
LL1.node_after(1,30)
LL1.node_before(5,1)
LL1.delete_by_value(1)
LL1.print_LL()
