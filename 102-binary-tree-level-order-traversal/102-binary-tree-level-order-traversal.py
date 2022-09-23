# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        queue = deque([root])
        res = []
        level = 0
        
        while queue:
            level = len(queue)
            children = []
        
            for _ in range(level):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
            
                
                if curr.right:
                    queue.append(curr.right)
        
                    
                children.append(curr.val)
            
            res.append(children)
        
                
        return res
            
                
            
        
            
        