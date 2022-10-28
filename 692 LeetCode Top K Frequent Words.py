class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        Map = {}
        for word in words:
            Map[word] = Map.get(word, 0)+1
        Map = sorted(Map.items(), key=lambda k:(-k[1], k[0]))
        ans = []
        for tup in Map:
            ans.append(tup[0])
            k-=1
            if k==0:
                break
            
        return ans
        
