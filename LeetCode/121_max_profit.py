# LeetCode 121. Best Time to Buy and Sell Stock


def maxProfit(prices: list[int]) -> int:
    curr_max = 0
    min_value = prices[0]
    for price in prices[1:]:
        min_value = min(price, min_value)
        curr_max = max(price - min_value, curr_max)
    return curr_max


if __name__ == "__main__":
    a = [10, 4, 2, 4, 9]
    assert maxProfit(a) == 7
