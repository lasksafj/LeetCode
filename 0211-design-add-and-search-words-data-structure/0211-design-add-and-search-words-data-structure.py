class WordDictionary:
    class Node:
        def __init__(self):
            self.next = {}
            self.eow = False
    
    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        r = self.root
        for w in word:
            if w not in r.next:
                r.next[w] = self.Node()
            r = r.next[w]
        r.eow = True

    def search(self, word: str) -> bool:
        def dfs(i, r):
            if not r:
                return False
            if i == len(word):
                return r.eow
            if word[i] == '.':
                for nr in r.next:
                    if dfs(i+1, r.next[nr]):
                        return True
                return False
            if word[i] in r.next:
                return dfs(i+1, r.next[word[i]])
            return False
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)