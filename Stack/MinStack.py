class MinStack:

    def __init__(self):
        self.stor = []
        self.minNums = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stor.append(val)
        self.min = min(val, self.min)
        self.minNums.append(self.min)

    def pop(self) -> None:
        del self.stor[-1]
        del self.minNums[-1]
        if self.minNums:
            self.min = self.minNums[-1]

    def top(self) -> int:
        return self.stor[-1]

    def getMin(self) -> int:
        print(self.stor)
        return self.min
