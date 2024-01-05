def update(s):
    i = 0
    while i < len(s):
        j = i+1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j-i >= 3:
            return update(s[:i] + s[j:])
        i = j
    return s

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        @cache
        def dfs(s,hand):
            # print(s,hand)
            if not s:
                return 0
            if not hand:
                return inf
            res = inf
            for i,ch in enumerate(hand):
                if i == 0 or ch != hand[i-1]:
                    hh = hand[:i] + hand[i+1:]
                    for j in range(len(s)):
                        if (ch == s[j] and (j == 0 or (j and s[j] != s[j-1]))) or (j and s[j] == s[j-1]):
                            # print('111',s[:j] + ch + s[j:], ch, hand)
                            tmp = update(s[:j] + ch + s[j:])
                            # print('222',tmp)
                            res = min(res, dfs(tmp, hh) + 1)
            # print(s,hand,'----',res)
            return res
        res = dfs(board, ''.join(sorted(hand)))
        return res if res < inf else -1