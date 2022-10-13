# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(cur, leftBound, rightBound):
            if not cur:
                return True
            if not (leftBound < cur.val < rightBound):
                return False
            
            if not isValid(cur.left, leftBound, cur.val):
                return False
            
            if not isValid(cur.right, cur.val, rightBound):
                return False
            
            return True
        
        return isValid(root, float('-inf'), float('inf'))