# LeetCode 49. Group Anagrams
from collections import defaultdict


# O(n*k*logk), where n - number of words, k - length of words
def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        sw = "".join(sorted(word))
        result[sw].append(word)
    return list(result.values())


# O(n*k)
def group_anagrams_2(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        representation = [0]*26
        for letter in word:
            representation[ord(letter) - ord("a")] += 1
        result[tuple(representation)].append(word)
    return list(result.values())


if __name__ == "__main__":
    assert group_anagrams_2(["abc"]) == [["abc"]]
    assert group_anagrams_2(["ab", "ba", "aba", "baa", "aab"]) == [['ab', 'ba'], ['aba', 'baa', 'aab']]