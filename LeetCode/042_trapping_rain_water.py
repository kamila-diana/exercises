# 42. Trapping Rain Water

def trap(height: list[int]) -> int:
    water = 0
    start = 0
    end = len(height) - 1
    right_max = 0
    left_max = 0
    while start <= end:
        if left_max > right_max:
            water += max(min(right_max, left_max) - height[end], 0)
            right_max = max(height[end], right_max)
            end -= 1
        else:
            water += max(min(right_max, left_max) - height[start], 0)
            left_max = max(height[start], left_max)
            start += 1
    return water


if __name__ == "__main__":
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trap(a) == 6
