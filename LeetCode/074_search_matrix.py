# LeetCode 74. Search a 2D Matrix

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    def search(nums: list[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while end > start + 1:
            middle = (end + start) // 2
            if nums[middle] == target:
                return True
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        if target == nums[end]:
            return True
        elif target == nums[start]:
            return True
        else:
            return False

    from functools import reduce
    one_list = reduce(lambda a, b: a + b, matrix)
    return search(one_list, target)


if __name__ == "__main__":
    assert not searchMatrix([[1, 2]], 5)
    assert searchMatrix([[-1, 0, 2], [4, 6, 7]], 4)
