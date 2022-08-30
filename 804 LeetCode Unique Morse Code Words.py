class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                 'p','q','r','s','t','u','v','w','x','y','z']
        symbols = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                   ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                   ".--","-..-","-.--","--.."]
        morse = dict(zip(alphas,symbols))
        res=0
        l1=[]
        for i in words:
            str1=""
            for j in i:
                str1+=morse[j]
            l1.append(str1)
        l1 = set(l1)
        return len(l1)
