class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

   

def lca(root,n1,n2):
    if root is None:
        return False
    if root.data==n1 or root.data ==n2:
        return root 
    left_lca=lca(root.left,n1,n2)
    right_lca=lca(root.right,n1,n2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print (lca(root, 6, 4).data)