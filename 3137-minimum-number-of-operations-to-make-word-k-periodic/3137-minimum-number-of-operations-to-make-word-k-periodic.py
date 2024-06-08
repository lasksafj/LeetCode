class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        mp = defaultdict(int)
        ma = 0
        for i in range(0, len(word), k):
            mp[word[i:i+k]] += 1
            ma = max(ma, mp[word[i:i+k]])
        
        return len(word)//k-ma