# LeetCode 424. Longest Repeating Character Replacement
from collections import defaultdict


# def number_of_other_chars(curr_letters):
#     max_value = 0
#     all_sum = 0
#     for key, value in curr_letters.items():
#         all_sum += value
#         max_value = max(value, max_value)
#     return all_sum - max_value
#

def characterReplacement(s: str, k: int) -> int:
    def number_of_other_chars(curr_letters):
        max_value = 0
        all_sum = 0
        for key, value in curr_letters.items():
            all_sum += value
            max_value = max(value, max_value)
        return all_sum - max_value

    curr_letters = defaultdict(lambda: 0)
    start = 0
    max_length = 0
    for (end, letter) in enumerate(s):
        if number_of_other_chars(curr_letters) < k:
            end += 1
            curr_letters[letter] += 1
            max_length = max(max_length, end - start)
        else:
            curr_letters[s[start]] -= 1
            start += 1
    return max_length


if __name__ == "__main__":
    a = "AABABBA"
    print(characterReplacement(a, 1))
