# 행성터널
# MST
# 시간초과

"""
import pytest


@pytest.mark.parametrize("n, xyz, expected",
                         [(5, [[11, -15, -15], [14, -5, -15], [-1, -1, -5], [10, -4, -1], [19, -4, 19]], 4)])


def test(n, xyz, expected):
    answer = solution(n, xyz)
    assert answer == expected
"""

def solution(n, xyz):
    total_cost = 0

    T = []
    T.append(0)

    while len(T) != n:
        lowest_cost = float('inf')
        next_planet = -1

        for current_planet in T:
            for i in range(n):
                if i not in T:
                    xa, ya, za = xyz[current_planet]
                    xb, yb, zb = xyz[i]
                    cost = min((abs(xa-xb),abs(ya-yb),abs(za-zb)))
                    if cost < lowest_cost:
                        lowest_cost = cost
                        next_planet = i

        if lowest_cost != float('inf'):
            total_cost += lowest_cost
            T.append(next_planet)

    return total_cost

if __name__ == "__main__":
    n = int(input())

    xyz = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        xyz.append(temp)

    print(solution(n, xyz))
