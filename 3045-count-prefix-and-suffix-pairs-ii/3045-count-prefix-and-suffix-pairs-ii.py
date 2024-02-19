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
                
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z
                
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for w in words:
            Z = z_function(w)
            Z[0] = len(w)
            cur = trie.root
            
            for i in range(len(w)):                    
                ch = w[i]
                if ch in cur.next:
                    cur = cur.next[ch]
                    res += cur.cnt if Z[len(w)-i-1] == i+1 else 0
                else:
                    break
            trie.add(w)
            # print(res)
        return res
                