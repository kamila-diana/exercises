# LeetCode 567. Permutation in String
from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    expected_counter = Counter(s1)
    start = 0
    end = len(s1)
    curr_counter = Counter(s2[:end])
    while end < len(s2) + 1:
        if curr_counter == expected_counter:
            return True
        else:
            curr_counter[s2[start]] -= 1
            if curr_counter[s2[start]] == 0:
                curr_counter.pop(s2[start])
            start += 1
            if end < len(s2):
                curr_counter[s2[end]] += 1
            end += 1
    return False


if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo")
    assert not checkInclusion("ab", "eidboaoo")
