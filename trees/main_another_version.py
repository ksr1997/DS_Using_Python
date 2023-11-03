class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
        
    def insertData(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insertData(data)
            elif data >self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insertData(data)
        else:
            self.data=data
            
    #left root right
    def inorderTraversal(self,root):
        res=[]
        if root:
            res=self.inorderTraversal(root.left)
            res.append(root.data)
            res=res+self.inorderTraversal(root.right)
        return res
    
    #root left right
    def preorderTraversal(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.preorderTraversal(root.left)
            res=res+self.preorderTraversal(root.right)
        return res
    
    #left right root
    def postorderTraversal(self,root):
        res=[]
        if root:
            res=self.postorderTraversal(root.left)
            res=res+self.postorderTraversal(root.right)
            res.append(root.data)
        return res
    
    def findVal(self,val):
        if val<self.data:
            if self.left is None:
                return "Not found"
            return self.left.findVal(val)
        elif val>self.data:
            if self.right is None:
                return "Not found"
            return self.right.findVal(val)
        else:
            return "value found"
        
root = Node(27)
root.insertData(14)
root.insertData(35)
root.insertData(10)
root.insertData(19)
root.insertData(31)
root.insertData(42)
root.printTree()

#left root right or straight line vertical
inorder_list=root.inorderTraversal(root)
print(inorder_list)

#root left right
preorder_list=root.preorderTraversal(root)
print(preorder_list)

#left right root
postorder_list=root.postorderTraversal(root)
print(postorder_list)

print(root.findVal(10))