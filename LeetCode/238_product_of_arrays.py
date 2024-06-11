# LeetCode 238. Product of Array Except Self

# O(n) and O(n) in memory
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    sufix = [1] * n
    for i in range(n - 1):
        prefix[i + 1] = prefix[i] * nums[i]
    for i in range(n - 1):
        sufix[n - i - 2] = sufix[n - i - 1] * nums[n - i - 1]
    return [prefix[i]*sufix[i] for i in range(n)]


# O(n) and O(1) in memory
def product_except_self_2(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n
    for i in range(n - 1):
        result[n - i - 2] = result[n - i - 1] * nums[n - i - 1]
    prefix = 1
    for i in range(n):
        result[i] *= prefix
        prefix *= nums[i]
    return result


if __name__ == "__main__":
    example = [2, 3, 5, 7]
    print(product_except_self_2(example))
    print("OK")
