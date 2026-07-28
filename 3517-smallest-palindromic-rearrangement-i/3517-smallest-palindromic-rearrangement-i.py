class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mp = Counter(s)
        mid = ''
        for k,v in list(mp.items()):
            if v&1:
                v -= 1
                mid = k
        res = ''
        for k,v in sorted(mp.items()):
            res += k*(v//2)
        return res + mid + res[::-1]