class Solution:
    def clearStars(self, s: str) -> str:
        res = list(s)
        mp = [[] for _ in range(26)]
        for i,c in enumerate(s):
            if c != '*':
                mp[ord(c)-97].append(i)
            else:
                res[i] = ''
                for k in range(26):
                    if mp[k]:
                        res[mp[k].pop()] = ''
                        break
        return ''.join(res)