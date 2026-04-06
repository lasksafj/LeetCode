class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y = 0,0
        dx,dy = 0,1
        obstacles = set((a,b) for a,b in obstacles)
        res = 0
        for d in commands:
            if d == -2:
                dx,dy = -dy,dx
            elif d == -1:
                dx,dy = dy,-dx
            else:
                k = 1
                while k <= d and (x+k*dx,y+k*dy) not in obstacles:
                    k += 1
                k -= 1
                x,y = x+k*dx,y+k*dy
            res = max(res, x**2 + y**2)
        return res