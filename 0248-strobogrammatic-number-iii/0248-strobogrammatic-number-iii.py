class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        q, res, low, high, ln = deque(["", "0", "1", "8"]), 0, int(low), int(high), len(high)
        while q:
            s = q.popleft()
            if s and s[0] != '0' and low <= int(s) <= high:
                res += 1
            for l,r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0")):
                if len(s)+2 > ln:
                    break
                q.append(l+s+r)
        return res if low != 0 else res+1