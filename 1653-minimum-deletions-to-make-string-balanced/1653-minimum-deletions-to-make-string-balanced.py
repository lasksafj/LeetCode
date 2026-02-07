class Solution:
    def minimumDeletions(self, s: str) -> int:
        # a = s.count('a')
        # if a == len(s): return 0
        # b = 0
        # res = inf
        # for c in s:
        #     if c == 'a':
        #         a -= 1
        #     else:
        #         res = min(res, a+b)
        #         b += 1
        # return min(res, a+b)
        dp = 0 # min no deletions to make balance string ...i
        b = 0
        for c in s:
            if c == 'b':
                b += 1
            else:
                dp = min(dp+1, b)
        return dp