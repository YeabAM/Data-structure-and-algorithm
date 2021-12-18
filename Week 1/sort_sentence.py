class Solution:
    def sortSentence(self, s: str) -> str:
        temp= s.split()
        word={}
        sentence=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            sentence=sentence+''.join(word[i])+' '
        sentence=sentence[:-1]
        return sentence