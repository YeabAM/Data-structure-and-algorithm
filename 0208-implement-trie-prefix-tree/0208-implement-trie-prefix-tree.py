class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def insert(self, word: str) -> None:
        root = self
        
        for ch in word:
            
            if ch in root.children:
                root = root.children[ch]
            else:
                new_node = Trie()
                root.children[ch] = new_node
                root = new_node
            
        root.is_end = True
                 

    def search(self, word: str) -> bool:
        root = self
        
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
            
        return root.is_end
            
    
    def startsWith(self, prefix: str) -> bool:
        root = self
    
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
            
        return True
        
        
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)