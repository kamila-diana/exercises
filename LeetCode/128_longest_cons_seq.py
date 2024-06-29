# LeetCode 128. Longest Consecutive Sequence

def longest_consecutive(nums: list[int]) -> int:
    numbers = set(nums)
    max_len = 0
    starts = set()
    for n in numbers:
        if n-1 not in numbers:
            starts.add(n)
    for s in starts:
        i = 1
        while s+i in numbers:
            i += 1
        max_len = max(max_len, i)
    return max_len


if __name__ == "__main__":
    nums = [4, 1, 3, 2, 8, 10, 9, 5, 6, 7]
    assert longest_consecutive(nums) == 10
