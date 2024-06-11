# LeetCode 36. Valid Sudoku

def only_numbers(l):
    return list(filter(lambda x: x != ".", l))


def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        numbers = only_numbers(row)
        if len(numbers) != len(set(numbers)):
            return False

    for i in range(9):
        numbers = only_numbers(list(map(lambda x: x[i], board)))
        if len(numbers) != len(set(numbers)):
            return False

    for i in range(3):
        for j in range(3):
            square = []
            for n in range(3):
                for m in range(3):
                    square.append(board[3*i + n][3*j + m])
            print(square)
            numbers = only_numbers(square)
            if len(numbers) != len(set(numbers)):
                return False

    return True


if __name__ == "__main__":
    example_1 =\
         [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert isValidSudoku(example_1)

    example_2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert not isValidSudoku(example_2)
