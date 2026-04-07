class Robot:

    def __init__(self, width: int, height: int):
        self.x,self.y = 0,0
        self.dx,self.dy = 1,0
        self.w = width-1
        self.h = height-1

    def step(self, num: int) -> None:
        x,y,dx,dy,w,h = self.x,self.y,self.dx,self.dy,self.w,self.h
        num %= 4*(w+h)
        while num:
            nx,ny = max(0, min(x+num*dx,w)), max(0, min(y+num*dy,h))
            if dx != 0:
                k = (nx-x)//dx
            else:
                k = (ny-y)//dy
            if k < num:
                dx,dy = -dy,dx
            x,y = nx,ny
            num -= k

        self.x,self.y,self.dx,self.dy = x,y,dx,dy

    def getPos(self) -> List[int]:
        return self.x,self.y

    def getDir(self) -> str:
        if (self.dx,self.dy) == (1,0):
            return 'East'
        elif (self.dx,self.dy) == (0,1):
            return 'North'
        elif (self.dx,self.dy) == (-1,0):
            return 'West'
        else:
            return 'South'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()