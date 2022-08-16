class Trie:
    def __init__ (self):
        self.children = {}
        self.isEndOfWord = False
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        pref = []
        res = []
        
        def insert(word):
            curr = root

            for i in range(len(word)):
                if word[i] in curr.children:
                    curr = curr.children[word[i]]
                else:
                    newNode = Trie()
                    curr.children[word[i]] = newNode
                    curr = newNode

            curr.isEndOfWord = True

        def startsWith(prefix):
            curr = root
            pref = []

            for i in range(len(prefix)):
                if prefix[i] in curr.children:
                    pref.append(prefix[i])
                    curr = curr.children[prefix[i]]
                    if curr.isEndOfWord:
                        pref = "".join(pref)
                        # print(pref, prefix)
                        return pref
                else:
                    return None
        
            return "".join(pref)
        
        for word in dictionary:
            insert(word)
            
        words = sentence.split()
        for word in words:
            if startsWith(word):
                res.append(startsWith(word))
            else:
                res.append(word)
                
            # print(res)
                
            
                
                
        return ' '.join(res)