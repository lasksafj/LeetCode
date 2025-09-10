class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        languages = [set()] + [set(l) for l in languages]
        A = set()
        for a,b in friendships:
            if languages[a] & languages[b]:
                continue
            A.add(a)
            A.add(b)
        if not A: return 0
        res = inf
        for i in range(1,n+1):
            res = min(res, sum(i not in languages[a] for a in A))
        return res