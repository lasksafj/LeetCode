class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = {}
        for i,skill in enumerate(req_skills):
            m[skill] = 1<<i
        fin = 2**len(req_skills)-1
        @cache
        def dfs(i, d):
            if d == fin:
                return []
            if i == len(people):
                return [0]*100
            a = dfs(i+1, d)
            for s in people[i]:
                if s in m:
                    d |= m[s]
            b = dfs(i+1, d) + [i]
            return a if len(a) < len(b) else b
        return dfs(0,0)