# 167. Two Sum II - Input Array Is Sorted

def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1
    while i != j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i+1, j+1]
        elif s > target:
            j -= 1
        else:
            i += 1
    return []


if __name__ == "__main__":
    a = [2, 7, 11, 15]
    assert twoSum(a, 9) == [1, 2]
