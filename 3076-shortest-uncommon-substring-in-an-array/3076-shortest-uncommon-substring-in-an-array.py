class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = ['' for _ in range(len(arr))]
        for l in range(1, max(len(s) for s in arr)+1):
            mp = defaultdict(int)
            for s in arr:
                if len(s) >= l:
                    for i in range(len(s)-l+1):
                        mp[s[i:i+l]] += 1
            # print(l,mp)
            for cur,s in enumerate(arr):
                if len(s) >= l and res[cur] == '':
                    # print(s, mp)
                    for i in range(len(s)-l+1):
                        mp[s[i:i+l]] -= 1

                    for i in range(len(s)-l+1):
                        if mp[s[i:i+l]] == 0:
                            if res[cur] == '' or s[i:i+l] < res[cur]:
                                res[cur] = s[i:i+l]
                                
                    for i in range(len(s)-l+1):
                        mp[s[i:i+l]] += 1
        return res