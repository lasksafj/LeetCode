class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def getmask(word):
            res = 0
            for w in word:
                res |= 1 << (ord(w) - ord('a'))
            return res
        
        m = defaultdict(int)
        for word in words:
            m[getmask(word)] += 1
        res = []
        for puzzle in puzzles:
            puzzles_mask = getmask(puzzle[1:])
            a = puzzles_mask
            cnt = 0
            first_char = 1 << (ord(puzzle[0]) - ord('a'))
            while a > 0:
                cnt += m[a | first_char]
                a = (a-1) & puzzles_mask
            cnt += m[a | first_char]
            res.append(cnt)
        return res