# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        
        curr = root
        if not root:
            root = newNode
        
        while curr and curr.val != val:
            if curr.val > val:
                if not curr.left:
                    curr.left = newNode
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = newNode
                    break
                curr = curr.right
                
        return root
        