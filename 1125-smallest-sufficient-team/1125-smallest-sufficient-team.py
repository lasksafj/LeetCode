class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = {}
        for i,skill in enumerate(req_skills):
            m[skill] = 1<<i
        dp = [[] for _ in range(2**len(req_skills))]
        skills_mask_of_person = [0]*len(people)
        for i in range(len(people)):
            for s in people[i]:
                if s in m:
                    skills_mask_of_person[i] |= m[s]

        def dfs(d):
            if dp[d] != []:
                return dp[d]
            for i in range(len(people)):
                nd = d | skills_mask_of_person[i]
                if nd != d:
                    a = [i] + dfs(nd)
                    if dp[d] == [] or len(a) < len(dp[d]):
                        dp[d] = a
            return dp[d]
        return dfs(0)