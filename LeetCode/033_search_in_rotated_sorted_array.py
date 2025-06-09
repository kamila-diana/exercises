# LeetCode 33. Search in Rotated Sorted Array
def search(nums: list[int], target: int) -> int:
    def find_rotation():
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] < nums[start]:
                end = middle
            elif nums[end] < nums[middle]:
                start = middle
            else:
                return start
        if nums[end] < nums[start]:
            return end
        else:
            return start

    def find_target(start: int, end: int) -> int:
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle
            else:
                start = middle
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1

    rotation = find_rotation()
    part_1 = find_target(0, rotation - 1)
    part_2 = find_target(rotation, len(nums) - 1)
    return max(part_1, part_2)


if __name__ == "__main__":
    assert search([1, 2, 3, 4, 5, 6], 4) == 3
    assert search([3, 4, 5, 0, 1], 0) == 3
    assert search([3, 1, 2], 4) == -1
