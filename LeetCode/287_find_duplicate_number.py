# LeetCode 287. Find the Duplicate Number

def findDuplicate(nums: list[int]) -> int:
    slow, fast = 0, 0
    finished = False
    while not finished:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            finished = True

    new_slow = 0
    while new_slow != slow:
        new_slow = nums[new_slow]
        slow = nums[slow]
    return slow


if __name__ == "__main__":
    assert findDuplicate([3, 1, 3, 4, 2]) == 3
