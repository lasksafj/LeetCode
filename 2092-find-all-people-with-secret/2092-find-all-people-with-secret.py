def dfs(i, adj, res, vis):
    if i in vis:
        return
    res.add(i)
    vis.add(i)
    for ne in adj[i]:
        dfs(ne, adj, res, vis)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        A = sorted(meetings, key=lambda x:x[2])
        i = 0
        res = set()
        res.add(0)
        res.add(firstPerson)
        while i < len(A):
            j = i
            tmp = defaultdict(list)
            ok = False
            starts = set()
            while j < len(A) and A[j][2] == A[i][2]:
                a,b,_ = A[j]
                tmp[a].append(b)
                tmp[b].append(a)
                if a in res:
                    starts.add(a)
                if b in res:
                    starts.add(b)
                j += 1
            if starts:
                vis = set()
                for start in starts:
                    dfs(start, tmp, res, vis)
            i = j

        return res