class Solution:
    def appealSum(self, s: str) -> int:
        occur_pos = {}
        for c in string.ascii_lowercase:
            occur_pos[c] = -1
        prev, dp = 0,0
        for i in range(len(s)):
            prev += i - occur_pos[s[i]]
            dp += prev
            occur_pos[s[i]] = i
        return dp