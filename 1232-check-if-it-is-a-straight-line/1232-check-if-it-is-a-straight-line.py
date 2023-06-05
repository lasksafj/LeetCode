class Solution:
    def checkStraightLine(self, co: List[List[int]]) -> bool:
        dx,dy = co[0][0]-co[1][0], co[0][1]-co[1][1]
        for a,b in co[2:]:
            a,b = a-co[0][0], b-co[0][1]
            if a*dy != b*dx:
                return False
        return True