class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first = ListNode()
        self.last = ListNode()
        self.first.next = self.last
        self.last.prev = self.first
        self.mp = {}

    def add_tail(self, cur):
        last = self.last
        tail = last.prev
        tail.next = cur
        cur.prev = tail
        cur.next = last
        last.prev = cur

    def remove_node(self, cur):
        a = cur.prev
        b = cur.next
        a.next = b
        b.prev = a

    def get(self, key: int) -> int:
        mp = self.mp
        if key not in mp:
            return -1
        cur = mp[key]
        self.remove_node(cur)
        self.add_tail(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        mp = self.mp
        if key in mp:
            mp[key].val = value
            self.get(key)
        else:
            cur = ListNode(key, value)
            if len(mp) == self.capacity:
                node = self.first.next
                del mp[node.key]
                self.remove_node(node)
            self.add_tail(cur)
            mp[key] = cur

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)