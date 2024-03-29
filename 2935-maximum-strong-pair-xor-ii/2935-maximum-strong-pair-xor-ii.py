class TrieNode:
    def __init__(self):
        self.next = {}
        self.eow = False
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.next:
                cur.next[letter] = TrieNode()
            cur = cur.next[letter]
            cur.cnt += 1
        cur.eow = True
    
    def remove(self, word):
        cur = self.root
        for letter in word:
            prev = cur
            cur = cur.next[letter]
            cur.cnt -= 1
            if cur.cnt == 0:
                del prev.next[letter]
    

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def bin20(n):
            res = ['0']*20
            i = 0
            for c in bin(n)[2:][::-1]:
                res[i] = c
                i += 1
            return res
        def maxXor(n, trie):
            n = bin20(n)
            cur = trie.root
            res = 0
            for i in range(19,-1,-1):
                if n[i] == '1':
                    if '0' in cur.next:
                        cur = cur.next['0']
                        res += 1<<i
                    else:
                        cur = cur.next['1']
                else:
                    if '1' in cur.next:
                        cur = cur.next['1']
                        res += 1<<i
                    else:
                        cur = cur.next['0']
            return res
        
        trie = Trie()
        nums.sort()
        N = len(nums)
        j = 0
        res = 0
        for i in range(N):
            while j < N and nums[j] <= nums[i]*2:
                trie.add(bin20(nums[j])[::-1])
                j += 1
            res = max(res, maxXor(nums[i], trie))
            trie.remove(bin20(nums[i])[::-1])
        return res