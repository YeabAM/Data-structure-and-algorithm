class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                node = Trie()
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.isEndofWord = True

    def search(self, word: str, isPrefix = False) -> bool:
        curr = self.root
        
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
                
        
        return curr.isEndofWord or isPrefix
        
        

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)