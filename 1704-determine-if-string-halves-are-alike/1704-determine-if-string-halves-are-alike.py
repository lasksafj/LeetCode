class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        nov = 0
        for c in s[:len(s)//2]:
            if c in m:
                nov += 1
        for c in s[len(s)//2:]:
            if c in m:
                nov -= 1
                if nov < 0:
                    return False
        return nov == 0
        