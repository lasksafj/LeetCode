class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        x,y = -1,-1
        res = 0
        for a,b in intervals:
            if a > y:
                res += 2
                x,y = b-1,b
            elif a > x:
                x = b
                if x != y:
                    x,y = y,x
                else:
                    x,y = b-1,b
                res += 1
            # print(x,y,res)
        return res