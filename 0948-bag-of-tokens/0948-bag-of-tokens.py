class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        N = len(tokens)
        res = 0
        cnt = 0
        i,j = 0,N-1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                cnt += 1
                res = max(res, cnt)
                i += 1
            else:
                if cnt == 0:
                    return res
                power += tokens[j]
                j -= 1
                cnt -= 1
        return res