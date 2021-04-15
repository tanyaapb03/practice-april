



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def  insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data) 
            if data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
            
        else:
            self.data=data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()



def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+1+size(node.right))


def level(node):
    lev=0
    if node is None:
        return 0
    else:
        ldepth=level(node.left)
        rdepth=level(node.right)

    if ldepth > rdepth:
        lev=ldepth+1
    else:
        lev=rdepth+1


    return lev

            
def minimumval(node):
    curr=node
    mini=[]
    while curr.left !=None:
        mini.append(curr.data)
        curr=curr.left
    return min(mini)

def PrintPostorder(node):
    if node is None:
        return None
    
    PrintPostorder(node.left)
        
    PrintPostorder(node.right)

    print(node.data)
     
    
    
    

# ef haspathsum(node,sumi):
#     if node ==None:
#         return sumi==0
        
#     else:
#         subsum=sumi-node.data 
#         print(subsum)
#         return (haspathsum(node.left,subsum)or  haspathsum(node.right,subsum))
# def printpaths(node):
#     path=int[1000]d
#     helper(node,path,0)

# def helper(node,path,pathlen):

    # pathl=[node.data]
    # pathr=[node.data]
    # if node.left==True:
    #     pathl.append(node.left.data)
    #     print(pathl)
    #     helper(node.left)
    # if node.right==True:
    #     pathr.append(node.right.data)
    #     helper(node.right)
    # path=[pathl+pathr]
    # return path 

#     if node.data==None:

#         return 

#     path[pathlen]=node.data
#     pathlen+=1

#     if node.left==None and node.right==None:
#         printarray(path,pathlen)

#     else:
#         helper(node.left,path,pathlen)
#         helper(node.right, path, pathlen)

#     def printarray(path,pathlen):
#         for i in path :
#             print(i)
#             i=i+1


# def mirror(node):
#     # find the level > create a temp with help of which you flip the left and right at each level 
#     if node is None:
#         return 
#     else:
#         mirror(node.left)
#         mirror(node.right)
   

#         temp=node.left
#         node.left=node.right
#         node.right=temp 

#         # print(node.data)
        
#     return(node)

# def dup(node):
#     if node is None:
#        return
#     else:
#         dup(node.left)
#         dup(node.right)

#         oldleft=node.left
#         node.left=Node(node.data)
#         node.left.left=oldleft
#     return (node)



# def newNode(data):
#     node=Node(data)
#     return node


def compare(nodea,nodeb):
    if nodea is None and nodeb is None:
        return 0
    if nodea is None and nodeb is not None:
        return 0
    if nodea is not None and nodeb is not None:
        if nodea.data==nodeb.data:
            compare(nodea.left,nodeb.left )
            compare(nodea.right,nodeb.right)
            return True 
        
           






     
# root1 = newNode(10)
# root2 = newNode(100)
# root1.left = newNode(7)
# root1.right = newNode(15)
# root1.left.left = newNode(4)
# root1.left.right = newNode(9)
# root1.right.right = newNode(20)
  
# root2.left = newNode(70)
# root2.right = newNode(150)
# root2.left.left = newNode(40)
# root2.left.right = newNode(90)
# root2.right.right = newNode(200)



    
        
roota = Node(2)
roota.left = Node(1)
roota.right = Node(3)
rootb=Node(2)
rootb.left=Node(1)
rootb.right=Node(3)

rootb.right.left=Node(4)
# root.left.left  = Node(5)
# root.left.right = Node(5)
# root.left.left.left=Node(6)

  
# print(size(root))
# print(level(root))
# print(minimumval(root))
# print(PrintPostorder(root))
# print(haspathsum(root,15))
# print(printpaths(root))
# root.printtree()
# print("=============")
# mirror(root)
# root.printtree()
print("==============")
# dup(root)
# root.printtree()

# if (compare(roota,rootb)):
#     print("same")
# else:
#     print("no")
print(compare(roota,rootb))












