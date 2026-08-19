class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        mp = defaultdict(int)
        for i,j in reservedSeats:
            mp[i] |= 1<<j
        a = 0b1111 << 2
        b = 0b1111 << 4
        c = 0b1111 << 6
        d = a|c
        res = 0
        for i,k in mp.items():
            if d & k == 0: 
                res += 2
                continue
            for mask in [a,b,c]:
                if k & mask == 0:
                    res += 1
                    break
        return res + (n-len(mp))*2