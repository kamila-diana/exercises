# LeetCode 1. two sums
def two_sum(nums: list[int], target: int) -> list[int]:
    candidates = {}
    for i, n in enumerate(nums):
        if (target - n) in candidates:
            return [candidates[target - n], i]
        else:
            candidates[n] = i
    return []


if __name__ == "__main__":
    assert two_sum([1, 2, 6, 9], 7) == [0, 2]
    assert two_sum([1, 5, 4], 9) == [1, 2]
    print("OK")
