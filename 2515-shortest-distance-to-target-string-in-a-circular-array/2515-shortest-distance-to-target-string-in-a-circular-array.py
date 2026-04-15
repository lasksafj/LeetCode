class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = inf
        for t,w in enumerate(words):
            if w == target:
                res = min(res, len(words)-abs(t-startIndex), abs(t-startIndex))
        return res if res < inf else -1