# LeetCode 239. Sliding Window Maximum

# O(n*k)
def maxSlidingWindow_nk(nums: list[int], k: int) -> list[int]:
    from collections import Counter
    if k >= len(nums):
        return [max(nums)]
    counter = Counter(nums[:k])
    result = [max(counter)]
    print(counter)
    print(result)
    for i in range(1, len(nums) - k + 1):
        j = i + k - 1
        print(i, j)
        counter[nums[i - 1]] -= 1
        if counter[nums[i - 1]] == 0:
            counter.pop(nums[i - 1])
        counter[nums[j]] += 1
        print(counter, max(counter))
        result = result + [max(counter)]
    return result


# O(n)
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    from collections import deque
    dq = deque()

    for i in range(0, k):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
    result = [nums[dq[0]]]

    for i in range(k, len(nums)):
        if dq[0] == i - k:
            dq.popleft()
        while len(dq) > 0 and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        result.append(nums[dq[0]])
    return result


if __name__ == "__main__":
    assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert maxSlidingWindow([-1, 1], 1) == [-1, 1]
    assert maxSlidingWindow([1, -1], 1) == [1, -1]
    assert maxSlidingWindow([-1, 1], 2) == [1]
    assert maxSlidingWindow([7, 2, 4], 2) == [7, 4]
    assert maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
    assert maxSlidingWindow([-7, -8, 7, 5, 7, 1, 6, 0], 4) == [7, 7, 7, 7, 7]
