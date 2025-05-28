class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def find_k_ball(edges, k):
            adj = defaultdict(list)
            for a,b in edges:
                adj[a].append(b)
                adj[b].append(a)
            N = len(adj)
            sizes = [1]*N
            vis = set()
            ans = [0]*N
            def subtree_size(i,p):
                for ne in adj[i]:
                    if ne == p or ne in vis:
                        continue
                    sizes[i] += subtree_size(ne, i)
                return sizes[i]
            def find_centroid(i, p, root):
                for ne in adj[i]:
                    if ne == p or ne in vis:
                        continue
                    if sizes[ne]*2 > sizes[root]:
                        return find_centroid(ne, i, root)
                return i
            def find_distance(i, p, d, all_d):
                if d > k:
                    return
                if len(all_d) == d:
                    all_d.append(1)
                else:
                    all_d[d] += 1
                for ne in adj[i]:
                    if ne == p or ne in vis:
                        continue
                    find_distance(ne, i, d+1, all_d)
            def find_ans(i, p, d, cntAll, cntSub):
                if d > k:
                    return
                # subtract overcounts within each subtree of centroid
                ans[i] += cntAll[min(k-d, len(cntAll)-1)] - cntSub[min(k-d, len(cntSub)-1)]
                for ne in adj[i]:
                    if ne == p or ne in vis:
                        continue
                    find_ans(ne, i, d+1, cntAll, cntSub)
            def decompose(root):
                subtree_size(root, -1)
                centroid = find_centroid(root, -1, root)
                vis.add(centroid)
                maxlen = 1
                cntSub = {}

                for ne in adj[centroid]:
                    if ne in vis:
                        continue
                    all_d = [0]
                    find_distance(ne, centroid, 1, all_d)
                    cntSub[ne] = [0] * len(all_d)
                    for d in range(len(all_d)):
                        cntSub[ne][d] += cntSub[ne][d-1] + all_d[d]
                    maxlen = max(maxlen, len(all_d))
                cntAll = [1] * maxlen
                for ne in cntSub:
                    for d in range(maxlen):
                        cntAll[d] += cntSub[ne][min(d, len(cntSub[ne])-1)]
                ans[centroid] += cntAll[min(k, len(cntAll) - 1)]
                for ne in adj[centroid]:
                    if ne in vis:
                        continue
                    find_ans(ne, centroid, 1, cntAll, cntSub[ne])
                for ne in adj[centroid]:
                    if ne not in vis:
                        decompose(ne)
            decompose(0)
            return ans
        
        res1 = find_k_ball(edges1, k)
        ma2 = 1
        if k > 0:
            res2 = find_k_ball(edges2, k-1)
            ma2 = max(res2)
        elif k == 0:
            ma2 = 0
        return [r+ma2 for r in res1]