print("trees info")

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)    
    return node

# deletes the key and returns the new root
'''
Concept:
If 1:
Only one value
check root is none

If 2:
only one child
check value<root or value>root and iterate
   go upto (root==val)
   if left none,update or
   if right none, update

else 3:
Two Pointers:
Succ parent->root
Succ->root.right

loop through till succ.left is not none:
Succ parent=succ
Succ=Succ.left

Case: Remove 50     1st iteration  2nd iteration

    #       50      Succ Parent(50)
    #     /   \
    #    30   70    Succ(70)        Succ Parent(70)
    #   / \ / \
    # 20 40 60 80                   Succ(60)

Update Succ Parent(70) root left to Succ(60) right
Assign 60 to root
remove 60
return root

'''
def deleteNode(root, k):
    #Case 1
    # Base case
    if root is None:
        return root
    
    
    #Case 2
    if k<root.key:
        root.left = deleteNode(root.left, k)
        return root
    elif k>root.key:
        root.right = deleteNode(root.right, k)
        return root
    # We reach here when root is the node to be deleted.
    # If one of the children is empty
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
    
    
    #Case 3
    # If both children exist
    else:
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
            
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right     
            
        root.key = succ.key    
        del succ
        return root
    
if __name__ == '__main__':
    
    # Let us create following BST
    #      50
    #     /   \
    #    30   70
    #   / \ / \
    # 20 40 60 80
    
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder ")
    inorder(root)
    print("\nPreorder")
    preorder(root)
    print("\nPostorder: ")
    postorder(root) 
    
    
    print("\n\nDelete a Leaf Node: 20")
    root = deleteNode(root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    inorder(root)    
    print("\n\nDelete Node with single child: 70")
    root = deleteNode(root, 70)
    print("Modified BST tree after deleting single child Node:")
    inorder(root)    
    print("\n\nDelete Node with both child: 50")
    root = deleteNode(root, 50)
    print("Modified BST tree after deleting both child Node:")
    inorder(root)
