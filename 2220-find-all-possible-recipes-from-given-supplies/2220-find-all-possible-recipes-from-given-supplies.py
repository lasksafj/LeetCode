class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        ind = defaultdict(int)
        for r,A in zip(recipes,ingredients):
            for a in A:
                adj[a].append(r)
            ind[r] += len(A)
        recipes = set(recipes)
        q = deque(supplies)
        res = []
        while q:
            a = q.popleft()
            if a in recipes:
                res.append(a)
            for ne in adj[a]:
                ind[ne] -= 1
                if ind[ne] == 0:
                    q.append(ne)
        return res