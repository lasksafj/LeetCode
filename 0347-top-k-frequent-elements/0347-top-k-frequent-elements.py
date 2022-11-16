class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = [[freq, n] for n,freq in Counter(nums).items()]
        return [e for _,e in heapq.nlargest(k, A)]