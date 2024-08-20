class UF:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n))
        self.r = [0]*n
        self.sz = [1]*n
        self.B = [[0]*4 for _ in range(n)]

    def root(self, x):
        if x == self.f[x]:
            return x
        return self.root(self.f[x])
    
    def union(self, a,b):
        B = self.B
        a,b = self.root(a), self.root(b)
        if a == b:
            return
        father = b
        if self.r[a] < self.r[b]:
            self.f[a] = b
        elif self.r[a] > self.r[b]:
            self.f[b] = a
            father = a
        else:
            self.f[a] = b
            self.r[b] += 1
        B[father][0] = min(B[a][0], B[b][0])
        B[father][1] = min(B[a][1], B[b][1])
        B[father][2] = max(B[a][2], B[b][2])
        B[father][3] = max(B[a][3], B[b][3])

    def bound(self, x):
        return self.B[self.root(x)]
    
def circle_intersects_rectangle(cx, cy, r, rx, ry, w, h):
    if rx<=cx<=rx+w and ry<=cy<=ry+h:
        return True
    # Find the nearest point on the rectangle to the circle's center
    nearest_x = max(rx, min(cx, rx + w))
    nearest_y = max(ry, min(cy, ry + h))
    
    # Calculate the distance from the circle's center to this nearest point
    dx = cx - nearest_x
    dy = cy - nearest_y
    distance_squared = dx * dx + dy * dy
    
    # Check if the distance is less than or equal to the circle's radius squared
    return distance_squared <= r * r

def circle_intersections(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # No intersection cases
    if d > r1 + r2:
        return []
    if d < abs(r1 - r2):
        return []
    if d == 0 and r1 == r2:
        return []
    
    # Calculate intersection points
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d
    
    x4 = x3 + h * (y2 - y1) / d
    y4 = y3 - h * (x2 - x1) / d
    
    x5 = x3 - h * (y2 - y1) / d
    y5 = y3 + h * (x2 - x1) / d
    
    return (x4, y4), (x5, y5)

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        # print('----')
        N = len(circles)
        uf = UF(N)
        for i in range(N):
            xi,yi,ri = circles[i]
            if xi**2 + yi**2 <= ri**2: return False 
            if (xCorner-xi)**2 + (yCorner-yi)**2 <= ri**2: return False
            
            if 0<=xi<=xCorner and 0<=yi<=yCorner:
                if (xi-ri <= 0 and xi+ri >= xCorner)\
                or (yi-ri <= 0 and yi+ri >= yCorner)\
                or (xi-ri <= 0 and yi-ri <= 0)\
                or (xi+ri >= xCorner and yi+ri >= yCorner):
                    return False
            
            if xi >= xCorner+ri or yi > yCorner+ri: continue 

            uf.B[i] = [xi-ri,yi-ri,xi+ri,yi+ri]
        
        for i in range(N):
            xi,yi,ri = circles[i]
            if not circle_intersects_rectangle(xi,yi,ri, 0,0,xCorner,yCorner):
                continue
            for j in range(i):
                xj,yj,rj = circles[j]
                if not circle_intersects_rectangle(xj,yj,rj, 0,0,xCorner,yCorner):
                    continue
                
                A = circle_intersections(xi,yi,ri, xj,yj,rj)
                if not A:
                    continue
                (x1,y1),(x2,y2) = A
                if 0<=x1<=xCorner and 0<=y1<=yCorner and 0<=x2<=xCorner and 0<=y2<=yCorner:
                    uf.union(i,j)
                    
                    if (uf.bound(i)[0] <= 0 and uf.bound(i)[1] <= 0) \
                    or (uf.bound(i)[0] <= 0 and uf.bound(i)[2] >= xCorner) \
                    or (uf.bound(i)[1] <= 0 and uf.bound(i)[3] >= yCorner) \
                    or (uf.bound(i)[2] >= xCorner and uf.bound(i)[3] >= yCorner):
                        return False
            
        return True