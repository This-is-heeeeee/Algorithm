# 인구 이동

import pytest


@pytest.mark.parametrize("n,l,r,map,expected",
                         [(2, 20, 50, [[50, 30],
                                       [20, 40]], 1),
                          (2, 40, 50, [[50, 30],
                                       [20, 40]], 0),
                          (2, 20, 50, [[50, 30],
                                       [30, 40]], 1),
                          (5, 5, 10, [[10, 15, 20],
                                      [20, 30, 25],
                                      [40, 22, 10]], 2),
                          (4, 10, 50, [[10, 100, 20, 90],
                                       [80, 100, 60, 70],
                                       [70, 20, 30, 40],
                                       [50, 20, 100, 10]], 3)])
def test(n, l, r, map, expected):
    answer = solution(n, l, r, map)
    assert answer == expected


def bfs(idx, l, r, map, check_map):
    y, x = idx
    if check_map[y][x]:
        return [], check_map
    common_area = [(y, x)]
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    area = [None] * 4
    for i in range(4):
        try:
            diff = abs(map[y][x] - map[y+dy][x+dx])
            print(diff)
            if diff >= l and diff <= r:
                area[i], check_map = bfs((y + dy[i], x + dx[i]), l, r, map, check_map)
        except:
            continue

    for i in range(4):
        if area[i]:
            common_area += area[i]

    return common_area, check_map


def solution(n, l, r, map):
    check_map = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            area, _ = bfs((i, j), l, r, map, check_map)
            print(area)

    return

"""

if __name__ == "__main__":
    n,l,r = list(map(int, input().split()))
    _map = []
    for i in range(n):
        m = list(map(int, input().split()))
        _map.append(m)

    solution(n, l, r, _map)
"""

