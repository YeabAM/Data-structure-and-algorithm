# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def theif(isRobbed, node):
            if not node:
                return 0
            if (isRobbed, node) in memo:
                return memo[(isRobbed,node)]
            
            left, right = 0, 0
            if not isRobbed:
                left =  theif(True, node.left)
                right =  theif(True, node.right)
                
                value1 = left + right + node.val
                
                left =  theif(False, node.left)
                right =  theif(False, node.right)
                
                value2= left + right
                # print(node.val, value1, value2)
                memo[(isRobbed, node)] =  max(value1, value2)
                return max(value1, value2)
                
            if isRobbed:
                left =  theif(False, node.left)
                right =  theif(False, node.right)
    
                memo[(isRobbed, node)] = left, right
                return left + right
                
        memo = {}
        return (theif(False, root))
        # return max(theif(True, root), theif(False, root))
        