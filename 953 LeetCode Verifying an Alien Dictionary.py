class Solution:
    order_map = [0] * 26
    def isAlienSorted(self, words, order):
        for i in range(len(order)):
            self.order_map[ord(order[i]) - ord('a')] = i
        
        for i in range(1, len(words)):
            if not self.compare(words[i], words[i-1]):
                return False
        return True

    def compare(self, s1, s2):
        j = 0
        while j < len(s1) and j < len(s2):
            if s1[j] == s2[j]:
                j += 1
            elif self.order_map[ord(s1[j]) - ord('a')] > self.order_map[ord(s2[j]) - ord('a')]:
                return True
            else:
                return False
        if len(s1) < len(s2):
            return False
        return True
