# LeetCode 875. Koko Eating Bananas
def minEatingSpeed(piles: list[int], h: int) -> int:
    from math import ceil

    def is_enough(k):
        return sum([ceil(x / k) for x in piles]) <= h

    start = 1
    end = max(piles)

    while start + 1 < end:
        middle = (start + end) // 2
        if is_enough(middle):
            end = middle - 1
        else:
            start = middle + 1
    if is_enough(start):
        return start
    elif is_enough(end):
        return end
    else:
        return end + 1


if __name__ == "__main__":
    assert minEatingSpeed(piles=[1, 4, 3, 2], h=9) == 2
    assert minEatingSpeed(piles=[25, 10, 23, 4], h=4) == 25
