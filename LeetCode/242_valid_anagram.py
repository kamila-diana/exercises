# LeetCode 242. Valid Anagram
from collections import defaultdict, Counter


def is_anagram_1(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def dict_of_letters(word: str) -> dict[str, int]:
    letters = defaultdict(int)
    for letter in word:
        letters[letter] += 1
    return letters


def is_anagram_2(s: str, t: str) -> bool:
    return dict_of_letters(s) == dict_of_letters(t)


def is_anagram_3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    a = "kamila"
    b = "kamali"
    c = "kamala"
    assert is_anagram_1(a, b)
    assert not is_anagram_1(a, c)
