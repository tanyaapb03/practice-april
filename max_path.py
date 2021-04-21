# maximum path of binary tree 
INT_MIN = -2**32
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def maxPathSum(root):
    res = [INT_MIN]
    maxi(root, res)
    return res[0]

def maxi(root,res):
    
    if root is None :
         return 
   

    left=maxi(root.left,res)
    right=maxi(root.right,res)
    print(left,right)
    if root.left is not None and root.right is not None:
        res[0]=max(res[0],left+right+root.data)
        return max(left,right)+root.data

    if root.left is None :
        print(left)
        return right+root.data
    else:
        return left+root.data 

root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)


print( maxPathSum(root))