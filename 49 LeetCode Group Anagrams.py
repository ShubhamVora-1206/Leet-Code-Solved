class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for i in strs:
            sortedword = "".join(sorted(i))

            if sortedword in anagram:
                anagram[sortedword].append(i)
            else:
                anagram[sortedword] = [i]

        return list(anagram.values())