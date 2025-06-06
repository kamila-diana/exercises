# LeetCode 704. Binary Search

def search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while end > start + 1:
        middle = (end + start) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start
    else:
        return -1


if __name__ == "__main__":
    assert search([1, 2], 1) == 0
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
