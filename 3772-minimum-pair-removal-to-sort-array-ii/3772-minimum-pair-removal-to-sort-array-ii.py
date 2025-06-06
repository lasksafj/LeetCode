class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLL:
    def __init__(self):
        self.head = Node()  # sentinel head
        self.tail = Node()  # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self._length = 0

    def append(self, v):
        node = Node(v, self.tail.prev, self.tail)
        self.tail.prev.next = node  # link prev tail node's next to new node
        self.tail.prev = node
        self._length += 1
        return node

    def appendleft(self, v):
        node = Node(v, self.head, self.head.next)
        self.head.next.prev = node  # link old first node's prev to new node
        self.head.next = node
        self._length += 1
        return node

    def remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        self._length -= 1
        return node

    def pop(self):
        if self._length == 0:
            return False
        self.remove(self.tail.prev)
        return True

    def popleft(self):
        if self._length == 0:
            return False
        self.remove(self.head.next)
        return True
    def insert(self, node, v):
        if not node: 
            return self.appendleft(v)
        nnode = Node(v, node, node.next)
        node.next = nnode
        nnode.prev = nnode
        return nnode
    
    def next(self, node):
        return node.next if node.next != self.tail else None
    def prev(self, node):
        return node.prev if node.prev != self.head else None

    def __len__(self):
        return self._length

    def __str__(self):
        vals = []
        curr = self.head.next
        while curr != self.tail:
            vals.append(str(curr.val))
            curr = curr.next
        return "DoublyLinkedList[" + ", ".join(vals) + "]"

    

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        SL = SortedList([], key=lambda x: [x[0], x[1]])
        DL = DoublyLL()
        inv = 0
        for i in range(len(nums)):
            node = DL.append([nums[i], i])
            if i+1 < len(nums):
                SL.add([nums[i]+nums[i+1], i, node])
                if nums[i] > nums[i+1]:
                    inv += 1
        res = 0
        while inv:
            res += 1
            x, i, node = SL.pop(0)
            l = DL.prev(node)
            r = DL.next(node)
            
            inv -= node.val[0] > r.val[0]
            rr = DL.next(r)
            if l:
                SL.discard([l.val[0] + node.val[0], l.val[1], l])
                inv -= l.val[0] > node.val[0]
            if rr:
                SL.discard([r.val[0] + rr.val[0], r.val[1], r])
                inv -= r.val[0] > rr.val[0]

            node.val[0] += r.val[0]
            
            if l:
                inv += l.val[0] > node.val[0]
                SL.add([l.val[0] + node.val[0], l.val[1], l])
            if rr:
                inv += node.val[0] > rr.val[0]
                SL.add([node.val[0] + rr.val[0], node.val[1], node])
            DL.remove(r)
            
        return res