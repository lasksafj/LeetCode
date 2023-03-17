class Trie:
    class Node:
        def __init__(self):
            self.next = {}
            self.eow = False
    
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        r = self.root
        for c in word:
            if c in r.next:
                r = r.next[c]
            else:
                r.next[c] = self.Node()
                r = r.next[c]
        r.eow = True
        
    def search(self, word: str) -> bool:
        r = self.root
        for c in word:
            if c in r.next:
                r = r.next[c]
            else:
                return False
        return r.eow

    def startsWith(self, prefix: str) -> bool:
        r = self.root
        for c in prefix:
            if c in r.next:
                r = r.next[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)