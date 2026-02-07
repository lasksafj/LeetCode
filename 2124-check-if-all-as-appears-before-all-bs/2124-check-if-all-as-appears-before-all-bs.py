class Solution:
    def checkString(self, s: str) -> bool:
        has_b = False
        for c in s:
            if c == 'a' and has_b:
                return False
            has_b = c == 'b'
        return True