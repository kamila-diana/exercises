# LeetCode 76. Minimum Window Substring
from collections import Counter


def minWindow(s: str, t: str) -> str:
    def dict_is_sub_dict(in_dict, out_dict):
        if in_dict - out_dict == {}:
            return True
        else:
            return False

    letters = Counter(t)
    start = 0
    end = len(t)
    if dict_is_sub_dict(letters, Counter(s)):
        best_substring = s
    else:
        return ""
    curr_counter = Counter(s[start:end])
    while end < len(s) + 1 and start < len(s) - len(t) + 1:
        curr_substring = s[start:end]
        if dict_is_sub_dict(letters, curr_counter):
            if len(best_substring) > len(curr_substring):
                best_substring = curr_substring
            curr_counter[s[start]] -= 1
            start += 1
        else:
            if end < len(s):
                curr_counter[s[end]] += 1
            end += 1
    return best_substring


if __name__ == "__main__":
    assert minWindow("ADOBECODEBANC", "BANC") == "BANC"
