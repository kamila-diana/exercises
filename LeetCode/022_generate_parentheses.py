# LeetCode 22. Generate Parentheses
def generateParenthesis(n: int) -> list[str]:
    stack = [("(", 1, 0)]
    new_stack = []
    for i in range(1, 2*n):
        for element in stack:
            if element[1] > element[2]:
                new_stack.append((element[0] + ")", element[1], element[2] + 1))
            if element[1] < n:
                new_stack.append((element[0] + "(", element[1] + 1, element[2]))
        stack = new_stack.copy()
        new_stack = []
    return [element[0] for element in stack]


if __name__ == "__main__":
    assert generateParenthesis(1) == ['()']
    assert generateParenthesis(2) == ['()()', '(())']
