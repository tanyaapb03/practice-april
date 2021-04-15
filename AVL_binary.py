from bst import Node 




class solution():
    def avl(self,node):
        #diff between height of left and right is either 0,-1or +1

        if node is None :
            return
        ldepth=self.avl(node.left)
        rdepth=self.avl(node.right)

        if ldepth-rdepth==0 or ldepth-rdepth==-1 or ldepth-rdepth==1:
            return True 
        else:
            return False

x=solution()
m=x.avl([1,2,3,4,5,6])
print(m)
