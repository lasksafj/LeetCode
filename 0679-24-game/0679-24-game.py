class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(A):
            if len(A) == 1:
                return math.isclose(A[0], 24)
            for a,b,*rest in itertools.permutations(A):
                for x in {a+b, a-b, a*b, b and a/b}:
                    if dfs([x] + rest):
                        return True
            return False
        return dfs(cards)