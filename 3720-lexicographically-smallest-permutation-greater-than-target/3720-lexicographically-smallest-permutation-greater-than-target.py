class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s = [ord(c)-97 for c in s]
        target = [ord(c)-97 for c in target]
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for c in target:
            mp[c] -= 1
        for i in range(len(target)-1, -1, -1):
            c = target[i]
            mp[c] += 1

            # target[:i] cannot be formed.
            if min(mp.values()) < 0:
                continue
            
            # Find the smallest character greater than target[i].
            nxt = -1
            for d in range(c+1, 26):
                if mp[d]:
                    nxt = d
                    break
            if nxt == -1:
                continue
            
            mp[nxt] -= 1
            res = target[:i] + [nxt]
            for c in range(26):
                res += [c] * mp[c]
            return ''.join(chr(c+97) for c in res)
        return ''