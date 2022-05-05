class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.dictionary = {}
        
    def addWord(self, word: str) -> None:
        current = self.root
        if self.search(word):
            self.dictionary[word] += 1
            return
        else:
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.isWord = True 
            self.dictionary[word] = 1
        
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isWord
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        for word in words:
            self.addWord(word)
        
        _list = []
        result = []
        for key, value in self.dictionary.items():
            _list.append((value * -1,  key))
        _list.sort()
        
        for i in range(k):
            result.append(_list[i][1])
        return result