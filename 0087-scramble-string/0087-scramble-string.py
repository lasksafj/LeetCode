class Solution:
    dp = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) <= 1 or sorted(s1) != sorted(s2):
            return False
        s = s1 + " " + s2
        if s in self.dp:
            return self.dp[s]
        n = len(s1)
        for i in range(1,n):
            a = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
            b = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:n-i])
            if a or b:
                self.dp[s] = True
                return True
        self.dp[s] = False
        return False