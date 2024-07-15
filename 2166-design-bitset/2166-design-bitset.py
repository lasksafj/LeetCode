class Bitset:

    def __init__(self, size: int):
        self.A = [0]*size
        self.no_flip = 0
        self.no1 = 0

    def fix(self, idx: int) -> None:
        A = self.A
        if A[idx] ^ self.no_flip == 0:
            A[idx] ^= 1
            self.no1 += 1

    def unfix(self, idx: int) -> None:
        A = self.A
        if A[idx] ^ self.no_flip == 1:
            A[idx] ^= 1
            self.no1 -= 1

    def flip(self) -> None:
        self.no_flip ^= 1
        self.no1 = len(self.A) - self.no1

    def all(self) -> bool:
        return self.no1 == len(self.A)

    def one(self) -> bool:
        return self.no1 > 0

    def count(self) -> int:
        return self.no1

    def toString(self) -> str:
        return ''.join(str(a^self.no_flip) for a in self.A)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()