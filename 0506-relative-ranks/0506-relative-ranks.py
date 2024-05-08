class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        A = sorted(score)
        mp = {}
        for i,a in enumerate(A):
            mp[a] = str(len(A) - i)
        res = []
        for n in score:
            if n == A[-1]:
                res.append('Gold Medal')
            elif n == A[-2]:
                res.append('Silver Medal')
            elif n == A[-3]:
                res.append('Bronze Medal')
            else:
                res.append(mp[n])
        return res