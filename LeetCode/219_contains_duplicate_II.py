# LeetCode 219. Contains Duplicate II

# O(n)
def contains_duplicate_ii(nums: list[int], k: int) -> bool:
    seen = {}
    for i in range(0, len(nums)):
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return True
        else:
            seen[nums[i]] = i
    return False


if __name__ == "__main__":
    nums_1 = [1, 2, 2]
    nums_2 = [3, 4, 5, 7]
    assert contains_duplicate_ii(nums_1, 2)
    assert not contains_duplicate_ii(nums_2, 2)

