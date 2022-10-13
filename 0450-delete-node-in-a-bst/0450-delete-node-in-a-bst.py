# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if  root and root.val == key and not root.right and not root.left:
            return None
        def find_min(node):
            parent = node
            node = node.right
            temp = node
            while node.left:
                parent = node
                node = node.left
                    
            if temp.val == node.val:
                parent.right = node.right
            else:
                parent.left = node.right
                
            return node
        
        def find_max(node):
            parent = node
            node = node.left
            temp = node
            
            while node.right:
                parent = node
                node = node.right
            
            if temp.val == node.val:
                parent.left = node.left
            else:
                parent.right = node.left
            
            return node
        
        def traverse(node, parent):
            if not node:
                return
            if node.val == key:
                if node.right:
                    minn = find_min(node)
                    node.val = minn.val
                elif node.left:
                    maxx = find_max(node)
                    node.val = maxx.val
                else:
                    if parent.left and parent.left.val == node.val:
                        parent.left = None
                    if parent.right and parent.right.val == node.val:
                        parent.right = None
                    
            elif node.val > key:
                traverse(node.left, node)
            else:
                traverse(node.right, node)  
        traverse(root, TreeNode())
        return root