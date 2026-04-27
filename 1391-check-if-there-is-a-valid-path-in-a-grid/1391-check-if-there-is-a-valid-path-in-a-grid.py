class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M,N = len(grid),len(grid[0])
        in_out = {
            1: {'r':'r', 'l':'l'},
            2 : {'t':'t','d':'d'},
            3: {'r':'d','t':'l'},
            4: {'t':'r','l':'d'},
            5: {'r':'t','d':'l'},
            6: {'d':'r','l':'t'}
        }
        D = {
            (0,1):'r',(0,-1):'l',(1,0):'d',(-1,0):'t'
        }
        DD = {'r':(0,1),'l':(0,-1),'d':(1,0),'t':(-1,0)}
        def sol(dx,dy):
            x,y = 0,0
            vis = set()
            while (x,y) not in vis and (x,y) != (M-1,N-1):
                vis.add((x,y))
                a = grid[x][y]
                nx,ny = x+dx,y+dy
                if 0<=nx<M and 0<=ny<N:
                    b = grid[nx][ny]
                    out_a = D[dx,dy]
                    if out_a not in in_out[b]: break
                    out_b = in_out[b][out_a]
                    dx,dy = DD[out_b]
                    x,y = nx,ny
                else: break
            return (x,y) == (M-1,N-1)
        if grid[0][0] == 5: return False
        if grid[-1][-1] == 4: return False
        if grid[0][0] in [1,6]: return sol(0,1)
        elif grid[0][0] in [2,3]: return sol(1,0)
        return sol(0,1) or sol(1,0)
        
        