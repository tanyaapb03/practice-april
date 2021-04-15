# check it the subtree is the mirror of each other

class Treenode:
    def __init__(self):
        self.val=val 
        self.left=left
        self.right=right
class Solution:
    def mirror(self,root:Treenode):
        def check(root1:Treenode,root2:Treenode):
            if root1 is None and root2 is None:
                return True 
            else:
                if root1.val==root2.val:
                    return(check(root1.left,root2.right),check(root1.right,root2.left))
            return False
        return check(root,root)

s1=Solution()
first=s1.mirror([1,2,2,3,4,4,3]) 
print(first)

