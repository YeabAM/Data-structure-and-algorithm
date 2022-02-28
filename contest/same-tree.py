# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            print("first")
            return True
        elif not p or not q:
            print("second")
            return False
        print(p.val==q.val)
        if p.val == q.val:
            print(p.val==q.val)
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        else:
            print("third")
            return False
            
    
        