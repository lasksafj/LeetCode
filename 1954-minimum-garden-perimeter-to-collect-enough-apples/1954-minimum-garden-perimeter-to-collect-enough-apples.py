class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        l,r = 0,100000
        while l <= r:
            x = (l+r)//2
            if x*(x+1)*(4*x+2) >= neededApples:
                r = x-1
            else:
                l = x+1
        return l*8