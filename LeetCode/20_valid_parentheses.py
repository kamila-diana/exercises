# LeetCode 20. Valid Parentheses
def isValid(s: str) -> bool:
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for letter in s:
        if letter in pairs.keys():
            stack.append(letter)
        elif stack and letter == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    assert isValid("{({})}")
    assert not isValid("[")
