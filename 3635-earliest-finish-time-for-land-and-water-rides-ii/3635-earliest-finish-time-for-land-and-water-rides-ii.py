class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        A = [[x,x+d] for x,d in zip(landStartTime, landDuration)]
        B = [[x,x+d] for x,d in zip(waterStartTime, waterDuration)]
        res = inf
        min_time_A = min(A, key=lambda x:x[1])[1]
        for x,d in zip(waterStartTime, waterDuration):
            res = min(res, max(x,min_time_A) + d)
        min_time_B = min(B, key=lambda x:x[1])[1]
        for x,d in zip(landStartTime, landDuration):
            res = min(res, max(x,min_time_B) + d)
        return res