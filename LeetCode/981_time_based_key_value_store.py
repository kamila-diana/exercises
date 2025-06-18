# LeetCode 981. Time Based Key-Value Store
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        elements = self.values[key]
        result = ""
        start = 0
        end = len(elements) - 1
        while start <= end:
            middle = (start + end) // 2
            if elements[middle][0] <= timestamp:
                result = elements[middle][1]
                start = middle + 1
            else:
                end = middle - 1
        return result


if __name__ == "__main__":
    obj = TimeMap()
    key = "key"
    value = "value"
    timestamp = 1
    obj.set(key, value, timestamp)
    print(obj.values)
    param_2 = obj.get(key, timestamp)
