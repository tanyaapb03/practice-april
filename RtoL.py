# return all root to leaf path 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def rtl(root):
    if root is None :
     return 
    s=int
    s+=root.data
    output=[]
   
    
    print(root)
    if root.left==None and root.right==None:
       output.append(s.substring(2))
       return

    if root.left!=None:
        rtl(root.left)
    if root.right!=None:
        rtl(root.right)


       
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print (rtl(root))

