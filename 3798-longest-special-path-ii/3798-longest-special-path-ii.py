class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        adj = defaultdict(list)
        for a,b,w in edges:
            adj[a].append([b,w])
            adj[b].append([a,w])
        A = []
        last = defaultdict(lambda:-1)
        res = [0,1]
        def dfs(i, p, d, left):
            nonlocal res, A
            A.append(d)
            prev_last = last[nums[i]]

            if (left and prev_last > left[0]) or (len(left) < 2 and prev_last > -1):
                left.append(prev_last)
                left.sort()
                if len(left) > 2:
                    left = left[1:]
            # print(i, A, left, last)
            if len(left) == 2:
                nres = [d - A[left[0] + 1], len(A) - (left[0]+1)]
            else:
                nres = [d, len(A)]
            res = sorted([res, nres], key=lambda x:[-x[0], x[1]])[0]

            last[nums[i]] = len(A)-1

            for ne,w in adj[i]:
                if ne == p: continue
                dfs(ne, i, d+w, left[:])
            
            A.pop()
            last[nums[i]] = prev_last
        dfs(0, -1, 0, [])
        return res