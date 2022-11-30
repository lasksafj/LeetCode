class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        mfreq = {}
        for n,cnt in freq.items():
            if cnt not in mfreq:
                mfreq[cnt] = 1
            else:
                return False
        return True
            