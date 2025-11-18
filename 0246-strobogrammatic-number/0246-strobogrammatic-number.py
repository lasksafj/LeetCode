class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = [0,1,-1,-1,-1,-1,9,-1,8,6]
        res = ''
        for n in map(int, num):
            if n == -1: return False
            res += str(mp[n])
        return res[::-1] == num