class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join([chr( 25 - (sum(weights[ord(c)-97] for c in w ) % 26) + 97)  for w in words])