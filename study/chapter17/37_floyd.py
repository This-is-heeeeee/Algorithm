# 플로이드

import pytest


@pytest.mark.parametrize("n, m, buses, expected",
                         [(5, 14,
                           [[1, 2, 2],[1, 3, 3],[1, 4, 1],[1, 5, 10],[2, 4, 2],[3, 4, 1],[3, 5, 1],[4, 5, 3],[3, 5, 10],[3, 1, 8],[1, 4, 2],[5, 1, 7],[3, 4, 2],[5, 2, 4]],
                           [[0, 2, 3, 1, 4],[12, 0, 15, 2, 5],[8, 5, 0, 1, 1],[10, 7, 13, 0, 3],[7, 4, 10, 6, 0]])])


def test(n, m, buses, expected):
    answer = solution(n, buses)
    assert answer == expected


def solution(n, buses):
    floyd = [[float("inf")] * n for _ in range(n)]

    for bus in buses:
        i,j,c = bus

        if floyd[i-1][j-1]:
            floyd[i-1][j-1] = min(floyd[i-1][j-1],c)
        else:
            floyd[i-1][j-1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    for i in range(n):
        for j in range(n):
            if floyd[i][j] == float("inf"):
                floyd[i][j] = 0
            print(floyd[i][j], end=' ')
        print()

    return floyd

"""
if __name__ == "__main__":
    n = int(input())
    m = int(input())

    buses = []

    for _ in range(m):
        bus = list(map(int, input().split()))
        buses.append(bus)

    solution(n, buses)
"""