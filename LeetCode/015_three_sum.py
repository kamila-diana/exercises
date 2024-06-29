# 15. 3Sum

def three_sum(nums: list[int]) -> list[list[int]]:
    result = set()
    for j, target in enumerate(nums):
        candidates = {}
        for i in range(j+1, len(nums)):
            n = nums[i]
            if (-target - n) in candidates and i != candidates[-target - n] and j != candidates[-target - n]:
                result.add(tuple([-target-n, n, target]))
            else:
                candidates[n] = i
    deduplicated = set([tuple(sorted(x)) for x in result])
    return list([list(x) for x in deduplicated])


if __name__ == "__main__":
    a = [1, -2, 1, 0, -1]
    assert three_sum(a) == [[-1, 0, 1], [-2, 1, 1]]
