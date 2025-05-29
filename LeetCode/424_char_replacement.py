# LeetCode 424. Longest Repeating Character Replacement
from string import ascii_uppercase


def for_given_letter(letter: str, s: str, k: int):
    s_len = len(s)
    longest = 1
    counter = 0
    j = 0
    for i in range(0, s_len):
        while counter <= k and j < s_len:
            j = max(j, i)
            if s[j] != letter:
                counter += 1
            if counter <= k:
                longest = max(j - i + 1, longest)
            j += 1
        if s[i] != letter:
            counter -= 1
    return longest


def characterReplacement(s: str, k: int) -> int:
    s_len = len(s)
    if s_len <= 1:
        return s_len
    else:
        uppercase_letters = list(ascii_uppercase)
        result = 0
        for let in uppercase_letters:
            result = max(result, for_given_letter(let, s, k))
        return result


if __name__ == "__main__":
    assert characterReplacement("AABABBA", 1) == 4
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("ABAA", 0) == 2
    assert characterReplacement("AAAA", 0) == 4
    assert characterReplacement("BAAA", 0) == 3
    assert characterReplacement("BAAAB", 2) == 5
    assert characterReplacement("AAAAA", 5) == 5
