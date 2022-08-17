class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        sett = set()
        for word in words:
            res = []
            for ch in word:
                res.append(mapp[ord(ch) - 97])
            sett.add("".join(res))
        return len(sett)