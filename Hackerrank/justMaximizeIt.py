# https://www.hackerrank.com/challenges/maximize-it/problem
from typing import List


def just_maximize_it(lists: List[List[int]], m: int):
    s_values = {0}
    for list_ in lists:
        new_s_values = set()
        for prev_val in s_values:
            for num in list_:
                new_s_values.add((num**2 + prev_val) % m)
        s_values = new_s_values
    return max(s_values)


def test_just_maximize_it():
    lists1 = [[1]]
    m1 = 2
    assert just_maximize_it(lists1, m1) == 1
    m2 = 1_000
    lists2 = [
        [2, 5, 4],
        [3, 7, 8, 9],
        [5, 5, 7, 8, 9, 10],
    ]
    s2 = 206
    assert just_maximize_it(lists2, m2) == s2
    m3 = 6
    lists3 = [[2], [2]]
    s3 = 2
    assert just_maximize_it(lists3, m3) == s3
    lists4 = [[1]]
    m4 = 1
    assert just_maximize_it(lists4, m4) == 0


def parse_maximize_it_input():
    k_and_m_str = input()
    k, m = map(int, k_and_m_str.split(' '))
    lists = []
    for i in range(k):
        lists.append(list(map(int, input().split(' '))))
    return lists, m


def maximize_it():
    lists, m = parse_maximize_it_input()
    return just_maximize_it(lists, m)


if __name__ == '__main__':
    test_just_maximize_it()
    # print(parse_maximize_it_input())