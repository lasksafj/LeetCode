class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        m = defaultdict(set)
        for a,b in mappings:
            m[a].add(b)
        i = 0
        k = 0
        while i < (len(s)-len(sub)+1):
            no = False
            for j in range(len(sub)):
                if s[i+j] == sub[j] or s[i+j] in m[sub[j]]:
                    continue
                no = True
            if not no:
                return True
            i += 1
        return False