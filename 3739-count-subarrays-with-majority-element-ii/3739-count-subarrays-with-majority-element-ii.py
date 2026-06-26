class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # a:sl target end at i
        # la: len end at i


        # a-b/la-lb > 0.5
        # a-b > 0,5*(la-lb)
        # a-0.5*la > b-0.5*lb
        
        A = SortedList([0])
        res = 0
        la = a = 0
        mp = defaultdict(int)
        for i,n in enumerate(nums):
            a += n==target
            la += 1
            res += A.bisect_left(a-0.5*la)
            A.add(a-0.5*la)
        return res