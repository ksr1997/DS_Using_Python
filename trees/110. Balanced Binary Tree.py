'''
Given a binary tree, determine if it is height-balanced
height-balanced:
A height-balanced binary tree is a binary tree in which 
the depth of the two subtrees of every node never differs by more than one.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
'''

'''
logic:
subfunction
get max lenght of right and left and compare return True or False
'''

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        t=True
        def subfun(root: Optional[TreeNode])->int:
            nonlocal t;
            if root is None:
                return 0
            left=subfun(root.left)
            right=subfun(root.right)
            if abs(left-right)>=2:
                t=False
            return 1+max(left,right)
        subfun(root)
        return t
        