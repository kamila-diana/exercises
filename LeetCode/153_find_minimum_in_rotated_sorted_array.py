# LeetCode 153. Find Minimum in Rotated Sorted Array
def findMin(nums: list[int]) -> int:
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        middle = (start + end) // 2
        if nums[middle] < nums[start]:
            end = middle
        elif nums[end] < nums[middle]:
            start = middle
        else:
            return nums[start]
    return min(nums[start], nums[end])


if __name__ == "__main__":
    assert findMin([1, 2, 3, 4, 5, 6]) == 1
    assert findMin([3, 4, 5, 0, 1]) == 0
    assert findMin([3,1,2]) == 1
