class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ls,lg,rs,rg = '','','',''
        for i in range(len(s)):
            if s[i] == goal[i]: continue
            if ls == '':
                ls = s[i]
                lg = goal[i]
            elif rs == '':
                rs = s[i]
                rg = goal[i]
            else:
                return False
        if ls == lg == '':
            return max(Counter(s).values()) > 1
        return ls == rg and rs == lg
                