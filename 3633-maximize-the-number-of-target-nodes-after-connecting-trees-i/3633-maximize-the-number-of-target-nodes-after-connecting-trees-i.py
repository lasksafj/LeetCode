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
                all_d.append((i,d))
                for ne in adj[i]:
                    if ne == p or ne in vis:
                        continue
                    find_distance(ne, i, d+1, all_d)
            def decompose(root):
                subtree_size(root, -1)
                centroid = find_centroid(root, -1, root)
                vis.add(centroid)

                all_d = []
                find_distance(centroid, -1, 0, all_d)

                # no_node distance <= d to root (1 <= d <= k)
                cntAll = [0] * (k+1)
                for _,d in all_d:
                    cntAll[d] += 1
                for d in range(1, k+1):
                    cntAll[d] += cntAll[d-1]

                # add contributions via centroid
                for u,d in all_d:
                    ans[u] += cntAll[k-d]
                
                # subtract overcounts within each subtree of centroid
                for ne in adj[centroid]:
                    if ne in vis:
                        continue
                    sub_d = []
                    find_distance(ne, centroid, 1, sub_d)
                    cntSub = [0]*(k+1)
                    for _,d in sub_d:
                        cntSub[d] += 1
                    for d in range(1, k+1):
                        cntSub[d] += cntSub[d-1]
                    for u,d in sub_d:
                        ans[u] -= cntSub[k-d]

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