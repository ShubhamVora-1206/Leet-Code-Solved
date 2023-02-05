class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # helper function to check if a given word can be formed by concatenating 
        # two or more words in the input list
        def can(w,dit):
            for i in range(1,len(w)):
                # check the left part of the word
                lf=w[:i]
                # check the right part of the word
                rt=w[i:]
                if lf in dit:
                    # if left part of the word is in the input set, check if the right part is in the set
                    # or can be formed by concatenating other words in the set
                    if rt in dit or can(rt,dit):
                        return True
            return False
        # initialize an empty list to store concatenated words
        res=[]
        # create a set of all words from the input list to improve lookup time
        dit = set(list(words))
        for w in words:
            # check if the word can be formed by concatenating other words in the set
            if can(w,dit):
                # if it can, add it to the list of concatenated words
                res.append(w)
                
        return res
