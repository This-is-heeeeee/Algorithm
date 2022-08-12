# 어두운 길
# MST

import pytest


@pytest.mark.parametrize("N, M, XYZ, expected",
                         [(7, 11, [[0, 1, 7], [0, 3, 5], [1, 2, 8],
                                   [1, 3, 9], [1, 4, 7], [2, 4, 5],
                                   [3, 4, 15], [3, 5, 6], [4, 5, 8],
                                   [4, 6, 9], [5, 6, 11]], 51)])


def test(N, M, XYZ, expected):
    answer = solution(N, M, XYZ)
    assert answer == expected


def solution(N, M, XYZ):
    houses = [[] for _ in range(N)]
    costs = [[float('inf')] * N for _ in range(N)]
    total = 0

    for x,y,z in XYZ:
        houses[x].append(y)
        houses[y].append(x)
        costs[x][y] = z
        costs[y][x] = z
        total += z

    T = []
    T.append(0)
    total_cost = 0
    while len(T) != N:
        lowest_cost = float('inf')
        next_house = -1
        for current_house in T:
            for i in houses[current_house]:
                if i not in T:
                    if costs[current_house][i] < lowest_cost:
                        lowest_cost = costs[current_house][i]
                        next_house = i

        if lowest_cost != float('inf'):
            total_cost += lowest_cost
            T.append(next_house)


    return total - total_cost