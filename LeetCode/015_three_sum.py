# LeetCode 15. 3Sum

def three_sum(nums: list[int]) -> list[list[int]]:
    result = set()
    sorted_nums = sorted(nums)
    for target_index, target_value in enumerate(sorted_nums):
        i = target_index + 1
        j = len(sorted_nums) - 1
        while i < j:
            s = sorted_nums[i] + sorted_nums[j]
            if s == -target_value:
                result.add((target_value, sorted_nums[i], sorted_nums[j]))
                i += 1
            elif s < - target_value:
                i += 1
            else:
                j -= 1
    return [[x, y, z] for (x, y, z) in result]


if __name__ == "__main__":
    a = [1, -2, 1, 0, -1]
    b = [3, 0, -2, -1, 1, 2]
    assert three_sum(a) == [[-1, 0, 1], [-2, 1, 1]]
    assert three_sum(b) == [[-2, -1, 3], [-1, 0, 1], [-2, 0, 2]]