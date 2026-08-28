class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        def check(mp):
            return all(v >= 0 for v in mp.values())

        mp = Counter(s)
        mid = ''
        for c,v in mp.items():
            if v&1:
                if mid != '': return ''
                mid = c
        if mid != '':
            mp[mid] -= 1
        for c in list(mp.keys()):
            mp[c] //= 2
        half = len(target)//2
        for c in target[:half]:
            mp[c] -= 1
        
        if check(mp):
            res = target[:half] + mid + target[:half][::-1]
            if res > target:
                return res

        for i in range(half-1, -1, -1):
            mp[target[i]] += 1
            if not check(mp): continue
            nxt = ''
            for c in range(ord(target[i])+1, ord('z')+1):
                c = chr(c)
                if mp[c]:
                    nxt = c
                    break
            if nxt == '': continue
            mp[nxt] -= 1
            res = target[:i] + nxt
            for c in ascii_lowercase:
                res += c*mp[c]
            return res + mid + res[::-1]
        return ''