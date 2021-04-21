class Node:
    def __init__(self,data):
        self.data=data
        root.left=None
        root.right=None


def conversion(self,llist):
    rootInd=int(len(llist)/2)
    root=Node(llist[rootInd])
    # print(root)
    llist.pop(rootInd)
    return (root,llist)
def construction(self,root,llist):
    for x in llist:
        if x < root:
            left=self.construction(root.left,llist)
        if x> root :
            right=self.construction(root.right,llist)

        return (left,right)



     

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


print(conversion([1,2,3,4,5,6]))

