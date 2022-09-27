class Trie:
    def __init__(self):
        self.isEOW = False
        self.visited = 0
        self.children = {}

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]: 
        root = Trie()
        res  = []
        
        def insert(word):
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = Trie()
                cur = cur.children[letter]
                cur.visited += 1
            cur.isEOW = True
        
        def search(word):
            temp = root
            count = 0

            for char in word:
                if char in temp.children:
                    temp = temp.children[char]
                    count += temp.visited

            return count
        
        for word in words:
            insert(word)
            
        for word in words:
            curr = search(word)
            res.append(curr)
            
        return res