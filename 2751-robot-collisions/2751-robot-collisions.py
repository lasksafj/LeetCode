class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)
        P = sorted(list(range(N)), key=lambda x:positions[x])
        st = []
        for i in P:
            survive = True
            if directions[i] == 'L':
                while st and directions[st[-1]] == 'R':
                    if healths[st[-1]] < healths[i]:
                        st.pop()
                        healths[i] -= 1
                    else: 
                        if healths[st[-1]] > healths[i]:
                            healths[st[-1]] -= 1
                        else:
                            st.pop()
                        survive = False
                        break
            if survive:
                st.append(i)
        return [healths[i] for i in sorted(st)]