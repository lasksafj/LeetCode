class MyHashSet:
    
    def __init__(self):
        self.m = {}

    def add(self, key: int) -> None:
        self.m[key] = 1

    def remove(self, key: int) -> None:
        if key in self.m: 
            del self.m[key]

    def contains(self, key: int) -> bool:
        if key in self.m:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)