class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # [1,3,2,2,2,3,4,3,1] -> [(1,1),(3,1),(2,3),(3,1),(4,1),(3,1),(1,1)]
        boxes = tuple((k, len(list(g))) for k,g in groupby(boxes))
        
        @cache
        def dp(grps):
            if not grps:
                return 0
            num_left,len_grp_left = grps[0]
            grps = grps[1:]
            res = dp(grps) + len_grp_left**2
            
            for i, (num, len_grp) in enumerate(grps):
                if num == num_left:
                    res = max(res, dp(grps[:i]) + dp( ((num_left,len_grp_left+len_grp),) + grps[i+1:]) )
            return res
        return dp(boxes)