# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def theif(root):
            if not root:
                return (0, 0)

            left = theif(root.left)
            right = theif(root.right)
            # (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
            return (root.val + left[1] + right[1], max(left) + max(right))

        return max(theif(root))
    
    
    
    
"""
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
    
"""

    
    
        