# LeetCode 217. Contains Duplicate

# O(n)
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False


# O(n)
def contains_duplicate_2(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums_1 = [1, 2, 2]
    nums_2 = [3, 4, 5, 7]
    assert contains_duplicate_2(nums_1)
    assert not contains_duplicate_2(nums_2)
    print("OK")
