class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(inf)
        res = []
        start,end = nums[0],nums[0]
        for n in nums[1:]:
            if n > end+1:
                if start < end:
                    res.append(str(start)+"->"+str(end))
                else:
                    res.append(str(end))
                start = n
                end = n
            else:
                end = n
        return res