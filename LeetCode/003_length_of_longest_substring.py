# LeetCode 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    curr_string = set()
    start = 0
    for (end, letter) in enumerate(s):
        while letter in curr_string:
            curr_string.remove(s[start])
            start += 1
        curr_string.add(letter)
        max_len = max(max_len, len(curr_string))
    return max_len


if __name__ == "__main__":
    a = "abzxcvaaabcd"
    assert lengthOfLongestSubstring(a) == 6

