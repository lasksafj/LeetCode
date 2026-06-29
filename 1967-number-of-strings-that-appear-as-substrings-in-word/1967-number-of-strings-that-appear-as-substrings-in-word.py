from collections import deque
from typing import List

K = 26

class Vertex:
    def __init__(self, p, ch, depth):
        self.next = [0] * K
        self.terminal = False
        self.p = p
        self.pch = ch
        self.depth = depth
        self.link = 0
        self.next_terminal = 0
        self.pattern_indices = []

class AhoCorasick:
    def __init__(self):
        self.t = [Vertex(-1, '$', 0)]
        
    def add_string(self, s, idx):
        v = 0
        for ch in s:
            c = ord(ch) - ord('a')
            if not self.t[v].next[c]:
                self.t[v].next[c] = len(self.t)
                self.t.append(Vertex(v, ch, self.t[v].depth + 1))
            v = self.t[v].next[c]
        self.t[v].terminal = True
        self.t[v].pattern_indices.append(idx)  # Lưu lại index của pattern này
        
    def push_links(self):
        q = deque([0])
        while q:
            v = q.popleft()
            cur = self.t[v]
            link = self.t[cur.link]
            cur.next_terminal = cur.link if link.terminal else link.next_terminal
            for c in range(K):
                if cur.next[c]:
                    self.t[cur.next[c]].link = link.next[c] if v else 0
                    q.append(cur.next[c])
                else:
                    cur.next[c] = link.next[c]
                    
    def transition(self, idx, c):
        return self.t[idx].next[ord(c) - ord('a')]

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        aho = AhoCorasick()
        for i, p in enumerate(patterns):
            aho.add_string(p, i)
        aho.push_links()
        visited_patterns = [False] * len(patterns)
        
        cur = 0
        for ch in word:
            cur = aho.transition(cur, ch)
            match = cur
            while match:
                if aho.t[match].terminal:
                    for idx in aho.t[match].pattern_indices:
                        visited_patterns[idx] = True
                match = aho.t[match].next_terminal
        return sum(visited_patterns)