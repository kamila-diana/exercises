# Leetcode 48. Rotate Image
import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        r = n // 2 + 1  # rows to rotate
        c = math.ceil(n / 2)  # columns to rotate
        for i in range(0, r):
            for j in range(0, c):
                matrix[i][j], matrix[j][n - i], matrix[n - i][n - j], matrix[n - j][i] = \
                    matrix[n - j][i], matrix[i][j], matrix[j][n - i], matrix[n - i][n - j]


if __name__ == "__main__":
    matrix_1 = [
        [1, 2],
        [3, 4]
    ]
    s = Solution()
    s.rotate(matrix_1)
    assert matrix_1 == [
        [3, 1],
        [4, 2]
    ]

    matrix_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    s.rotate(matrix_2)
    assert matrix_2 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
