class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True       

    def search(self, word: str) -> bool:
        def dfs(i, current):            
            if i == len(word):
                return current.isWord

            if word[i] != '.':
                if word[i] not in current.children:
                    return False
                if dfs(i+1, current.children[word[i]]): return True
            else:
                for char in current.children:
                    if dfs(i+1, current.children[char]): return True
            return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)