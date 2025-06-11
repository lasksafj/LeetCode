class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        S = [set(r) for r in responses]
        mp = defaultdict(int)
        for s in S:
            for w in s:
                mp[w] += 1
        return min(mp.items(), key=lambda x:[-x[1], x[0]])[0]