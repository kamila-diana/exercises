# LeetCode 155. Min Stack

class MinStack:
    def __init__(self):
        self.min = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.min:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return None


if __name__ == "__main__":
    val = 42
    obj = MinStack()
    obj.push(val)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
