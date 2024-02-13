class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt = Counter()
        for w in words:
            cnt.update(Counter(w))
        # print(cnt)
        even,odd = 0,0
        for v in cnt.values():
            even += v//2 * 2
            odd += v%2
        res = 0
        for l in sorted(len(x) for x in words):
            even -= l//2 * 2
            if even < 0:
                return res
            if odd < 0:
                even -= 2
                odd += 2
            odd -= l%2
            res += 1
                
        
        return res