"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        curr = root
        if curr:
            res.append(root.val)
            
            for child in root.children:
                res =res + self.preorder(child)
                
        return res