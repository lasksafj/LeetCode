class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(prev, i):
            # leaf = True
            i0,i1 = nums[i],nums[i]^k
            res = [i0,-inf]
            first = True
            for ne in adj[i]:
                if ne != prev:
                    score0, score1 = dfs(i, ne)
                    ne0,ne1 = nums[ne],nums[ne]^k
                    if first:
                        res[0] = max(i0+score0, i0+score1)
                        res[1] = max(i1+score0+ne1-ne0, i1+score1+ne0-ne1)
                        first = False
                    else:
                        res = [max(res[0]+score0, res[0]+score1, res[1]+i0-i1+score0-ne0+ne1, res[1]+i0-i1+score1-ne1+ne0), max(res[1]+score0, res[1]+score1, res[0]+i1-i0+score0-ne0+ne1, res[0]+i1-i0+score1-ne1+ne0)]
                    # if i == 0:
                    #     print('---',res,i0,i1,ne0,ne1, res[0]+i1-i0+score0-ne0+ne1, res[0]+i1-i0+score1-ne1+ne0)
                    # leaf = False
                    
            # print(i, res)
            return res
        return max(dfs(-1,0))