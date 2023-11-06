'''
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot 
and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

'''
logic:
check root and subRoot Base conditions
define function for same trees
first check root and subroot both are same or not
second check root.left with subroot and root.right with subroot
iterate
'''

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_same(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check_same(p.left,q.left) and check_same(p.right,q.right)
               
        if not root:
            return False
        if not subRoot:
            return True
        if root.val == subRoot.val:
            if check_same(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        