class Node:
    def __init__(self, val=(-1,-1), prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node((-1, -1), None, None)
        self.tail = Node((-1,-1), self.head, None)
        self.head.next = self.tail
        self.length = capacity
        self.capacity = capacity
        self.lru = dict()

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        
        temp = self.lru[key]
        tempPrev = temp.prev
        tempNext = temp.next
        
        if not tempPrev.prev and not tempNext.next:
            return temp.val[1]
        
        if tempNext != self.tail:
            temp2 = self.tail.prev
            temp.next = self.tail
            temp.prev = temp2
            temp2.next = temp
            self.tail.prev = temp

            tempPrev.next = tempNext
            tempNext.prev = tempPrev
        
        return self.tail.prev.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            temp = self.lru[key]
            temp.val = (key, value)
            self.get(key)
            temp2 = self.lru[key]
            return
        
        if self.length == 0:
            del self.lru[self.head.next.val[0]]
            
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            
            self.length += 1
            
        new = Node((key, value), None, self.tail)
        self.lru[key] = new
        
        temp = self.tail.prev
        temp.next = new
        new.prev = temp
        self.tail.prev = new
        
        self.length -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)