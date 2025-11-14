class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class DL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def add_tail(self, node):
        p = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = p
        p.next = node
    def remove(self, node):
        p,n = node.prev,node.next
        p.next = n
        n.prev = p
    def remove_head(self):
        key = self.head.next.key
        self.remove(self.head.next)
        return key
    def empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.mp = {} # key -> [freq, node]
        self.freq = defaultdict(lambda: DL()) # freq -> DL
        self.cap = capacity
        self.mi = 1

    def inc_freq(self, key):
        mp = self.mp
        freq = self.freq
        f, node = mp[key]
        mp[key][0] += 1
        if f in freq:
            freq[f].remove(node)
        freq[f+1].add_tail(node)
        if freq[f].empty():
            del freq[f]
            if f == self.mi:
                self.mi += 1
        self.mi = min(self.mi, f+1)

    def get(self, key: int) -> int:
        mp = self.mp
        freq = self.freq
        if key not in mp: return -1
        self.inc_freq(key)
        return mp[key][1].val

    def put(self, key: int, value: int) -> None:
        mp = self.mp
        freq = self.freq
        if key not in mp:
            if len(mp) == self.cap:
                remove_key = freq[self.mi].remove_head()
                if freq[self.mi].empty():
                    del freq[self.mi]
                del mp[remove_key]
            mp[key] = [0, Node(key, value)]
        else:
            f,node = mp[key]
            node.val = value
        self.inc_freq(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)