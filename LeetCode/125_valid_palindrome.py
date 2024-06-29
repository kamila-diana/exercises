# 125. Valid Palindrome

def isPalindrome(s: str) -> bool:
    standard = list([x.lower() for x in s if x.isalpha()])
    n = len(standard)
    for i in range(n // 2):
        if standard[i] != standard[n - i - 1]:
            return False
    return True


if __name__ == "__main__":
    assert isPalindrome("lalalal")
