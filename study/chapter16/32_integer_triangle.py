# 정수 삼각형

import pytest


@pytest.mark.parametrize("n, triangle, expected",
                         [(5, [[7],[3, 8],[8, 1, 0],[2, 7, 4, 4],[4, 5, 2, 6, 5]], 30)])


def test(n, triangle, expected):
    answer = solution(n, triangle)
    assert answer == expected


def solution(n, triangle):
    for i in range(1, n):
        for j in range(i+1):
            temp = []

            if j - 1 >= 0:
                temp.append(triangle[i][j] + triangle[i-1][j-1])
            if j + 1 <= i :
                temp.append(triangle[i][j] + triangle[i - 1][j])

            triangle[i][j] = max(temp)

    result = max(triangle[-1])

    return result

"""
if __name__ == "__main__":
    n = int(input())
    triangle = []

    for _ in range(n):
        row = list(map(int, input().split()))
        triangle.append(row)

    print(solution(n, triangle))
"""