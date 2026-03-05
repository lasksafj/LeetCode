class Solution:
    def minOperations(self, s: str) -> int:
        e0,e1 = 0,0
        for d in s:
            e0, e1 = e1+(d!='0'), e0+(d!='1')
        return min(e0,e1)