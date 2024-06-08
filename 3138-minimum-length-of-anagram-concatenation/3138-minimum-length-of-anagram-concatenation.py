class Solution:
    def minAnagramLength(self, s: str) -> int:        
        def check(mi):
            a = sorted(s[0:mi])
            for i in range(mi,len(s),mi):
                if sorted(s[i:i+mi]) != a:
                    return False
            return True
        
        for i in range(len(s),1,-1):
            if len(s)%i == 0 and check(len(s)//i):
                return len(s)//i
        return len(s)