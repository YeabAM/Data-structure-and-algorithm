"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = defaultdict(lambda:None)
        org = head
        
        while org:
            val = org.val
            copy[org] = Node(val)
            org = org.next
            
        org = head
        
        while org:
            curr = copy[org]
            curr.next = copy[org.next]
            curr.random = copy[org.random]
            org = org.next
            
        return copy[head]
        
        