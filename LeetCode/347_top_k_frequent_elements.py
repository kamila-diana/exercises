# LeetCode 347. Top K Frequent Elements
from collections import defaultdict


def top_k_frequent_2(nums: list[int], k: int) -> list[int]:
    frequency = defaultdict(int)
    for elem in nums:
        frequency[elem] += 1
    reversed_frequency: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for (key, value) in frequency.items():
        reversed_frequency[value].append(key)
    count = 0
    result = []
    i = len(nums)
    while count < k:
        result.extend(reversed_frequency[i])
        count += len(reversed_frequency[i])
        i -= 1
    return result


if __name__ == "__main__":
    a = [1, 2, 2, 3, 4, 4, 4]
    # a = [-1,-1]
    x = top_k_frequent_2(a, 2)
    print(x)
    print("OK")
