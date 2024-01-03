class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        p = sorted(list(range(len(positions))), key=lambda x:positions[x])
        st = []
        i = 0
        res = []
        while i < len(p):
            idx = p[i]
            if directions[idx] == 'R':
                st.append([healths[idx], idx])
                i += 1
                continue
            
            while st and healths[idx] > st[-1][0]:
                healths[idx] -= 1
                st.pop()
            if st:
                if healths[idx] == st[-1][0]:
                    st.pop()
                else:
                    st[-1][0] -= 1
            else:
                res.append([healths[idx], idx])
            i += 1
        res.extend(st)
        return [a[0] for a in sorted(res, key=lambda x:x[1])]

                