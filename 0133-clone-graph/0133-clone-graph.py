"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        
        copiedNode = {}
        queue = deque()
        queue.append(node)
        copiedNode[node.val] = Node(node.val)
        
        while queue:
            currNode = queue.popleft()
            
            for orginalNeigh in currNode.neighbors:
                if orginalNeigh.val not in copiedNode:
                    copy = Node(orginalNeigh.val)
                    queue.append(orginalNeigh)
                    copiedNode[orginalNeigh.val] = copy
                    
                copiedNode[currNode.val].neighbors.append(copiedNode[orginalNeigh.val])
                    
                    
                    
        return copiedNode[1]
        