class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:    
        X = sorted([[ax1,ax2], [bx1,bx2]])
        diff_x = max(0, X[0][1] - X[1][0]) if X[1][1] > X[0][1] else X[1][1] - X[1][0]
        Y = sorted([[ay1,ay2], [by1,by2]])
        diff_y = max(0, Y[0][1] - Y[1][0]) if Y[1][1] > Y[0][1] else Y[1][1] - Y[1][0]
        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - diff_x*diff_y