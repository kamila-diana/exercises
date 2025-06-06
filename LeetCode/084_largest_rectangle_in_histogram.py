# LeetCode 84. Largest Rectangle in Histogram

def largestRectangleArea(heights: list[int]) -> int:
    best = 0
    n = len(heights)
    stack = [(heights[0], 0)]
    for i in range(1, n):
        if heights[i] > stack[-1][0]:
            stack.append((heights[i], i))
        elif heights[i] < stack[-1][0]:
            while stack and heights[i] < stack[-1][0]:
                (height, start) = stack.pop()
                width = i - start
                area = height*width
                best = max(best, area)
            if stack and stack[-1][0] == heights[i]:
                pass
            else:
                stack.append((heights[i], start))
        else:
            pass
    while stack:
        (height, start) = stack.pop()
        width = n - start
        area = height*width
        best = max(best, area)
    return best


if __name__ == "__main__":
    assert largestRectangleArea([1, 2]) == 2
    assert largestRectangleArea([3, 1]) == 3

