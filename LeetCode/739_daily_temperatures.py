# LeetCode 739. Daily Temperatures
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stack = [0]
    result = [0]*n
    for i in range(1, n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            result[j] = i-j
        stack.append(i)
    return result


if __name__ == "__main__":
    assert dailyTemperatures([1, 2, 3]) == [1, 1, 0]
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
