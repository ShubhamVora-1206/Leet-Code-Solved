class Trie:
    def __init__(self):
        self.children = {}
        self.refs = 0
    
    def insert(self, word, root):
        for char in word:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
            root.refs += 1
        root.children['#'] = '#'
    
    def remove(self, word, root):
        for char in word:
            root = root.children[char]
            root.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        trie = Trie()
        for word in words:
            trie.insert(word, trie)
        res = set()
        def backtrack(ri, cj, seen, node, word):
            if '#' in node.children: 
                res.add(word)
                trie.remove(word, trie)

            for i, j in directions:
                nr, nc = ri + i, cj + j
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and board[nr][nc] in node.children and node.children[board[nr][nc]].refs > 0:
                    seen.add((nr, nc))
                    backtrack(nr, nc, seen, node.children[board[nr][nc]], word + board[nr][nc])
                    seen.discard((nr, nc))
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    backtrack(i, j, {(i, j)}, trie.children[board[i][j]], board[i][j])
        return res
