class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        T = {}
        for f in folder:
            f = f.split('/')[1:]
            cur = T
            for s in f:
                if s not in cur:
                    cur[s] = {}
                cur = cur[s]
            cur['#'] = 1
        res = []
        for f in folder:
            cur = T
            ok = True
            for s in f.split('/')[1:][:-1]:
                cur = cur[s]
                if '#' in cur:
                    ok = False
                    break
            if ok:
                res.append(f)
        return res