class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x,y = y,x
        A = [0]*(n+1)
        for i in range(1,n+1):
            A[1] += 2   # node i can go all left and right, so every distance += 1
                        # 12i45, i->2:1, i->4:1, i->1:2, i->5:2, so res[1] += 2, res[2] += 2, ... 
                        # so update range [1,n] += 2 using diff array A
            
            A[min(i-1, abs(i-y)+1+x-1) + 1] -= 1 
                # i->1 then stop, 
                # so all distance larger than distance i->1 -= 1
                
            A[min(n-i, abs(i-x)+1+n-y) + 1] -= 1
                # i->n then stop
                
            A[min(abs(i-x), abs(i-y)+1) + 1] += 1
                # i->x then split into 2 ways,
                # so all distance after i->x += 1
            
            A[min(abs(i-y), abs(i-x)+1) + 1] += 1
                # i->y then split into 2 ways
                
            r = max(x-i, 0) + max(i-y, 0)
            A[r + (y-x)//2 + 1] -= 1
            A[r + (y-x+1)//2 + 1] -= 1
                # When go from x to y then go to the middle, it will stop in middle, 
                # When go from y to x then go to the middle, it will stop in middle
                
        for i in range(2,n+1):
            A[i] += A[i-1]
        return A[1:]
            