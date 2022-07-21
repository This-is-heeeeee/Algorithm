# 편집거리

import pytest


@pytest.mark.parametrize("A, B, expected",
                         [("cat", "cut", 1),
                          ("sunday", "saturday", 3)])


def test(A, B, expected):
    answer = solution(A, B)
    assert answer == expected


def solution(A, B):
    edit_distance = [[0] * (len(B)+1) for _ in range(len(A)+1)]

    for i in range(1, len(A) + 1):
        edit_distance[i][0] = i
    for j in range(1, len(B) + 1):
        edit_distance[0][j] = j

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                edit_distance[i][j] = edit_distance[i-1][j-1]
            else:
                edit_distance[i][j] = min(edit_distance[i-1][j] + 1, edit_distance[i][j-1] + 1, edit_distance[i-1][j-1] + 1)

    result = edit_distance[-1][-1]

    return result