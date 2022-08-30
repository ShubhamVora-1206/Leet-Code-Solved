class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def subSeq(word):
            pre = -1
            for c in word:
                if c not in index_map:
                    return False
                index = bisect_right(index_map[c],pre)
                if index==len(index_map[c]):
                    return False
                pre = index_map[c][index]
            return True
        index_map= defaultdict(list)
        for i,c in enumerate(s):
            index_map[c].append(i)
        ans=0
        for word in words:
            if subSeq(word):
                ans+=1
        return ans
