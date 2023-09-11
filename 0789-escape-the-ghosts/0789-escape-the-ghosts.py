class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = abs(target[0]) + abs(target[1])
        for a,b in ghosts:
            if abs(a-target[0]) + abs(b-target[1]) <= d:
                return False
        return True