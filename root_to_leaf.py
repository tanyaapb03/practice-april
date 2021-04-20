# Sum Root to Leaf Numbers 

class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None


def sumRoot(root):
    if root is None:
         return 


    return dfs(root,0,0)
    p=root.data
def dfs(root,num,sumi):

    if root is None:
         return sumi
    print(num)

    num=num*10+root.data
    print(num)

    if (root.left is None and root.right is None):
        sumi=sumi+num
        return sumi

    #sumi=left subtree+right subtree
    sumi=dfs(root.left,num,sumi)+dfs(root.right,num,sumi)
    return sumi


    
   



root = Node(10)
root.left = Node(26)
root.right = Node(35)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)


print(sumRoot(root))