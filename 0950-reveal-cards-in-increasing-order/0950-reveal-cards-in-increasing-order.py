class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        res = deque(deck[:2])
        for n in deck[2:]:
            res.append(res.popleft())
            res.append(n)
        return list(res)[::-1]