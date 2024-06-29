# LeetCode 11. Container With Most Water

def maxArea(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    max_area = 0
    while i != j:
        curr_area = (j - i) * min(height[i], height[j])
        max_area = max(max_area, curr_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
