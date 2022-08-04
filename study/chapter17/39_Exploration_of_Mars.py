# 화성 탐사


import pytest


@pytest.mark.parametrize("n, map, expected",
                         [(3, [[5,5,4],[3,9,1],[3,2,7]], 20),
                          (5, [[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]], 19),
                          (7, [[9,0,5,1,1,5,3],[4,1,2,1,6,5,3],[0,7,6,1,6,8,5],[1,1,7,8,3,2,3],[9,4,0,7,6,4,1],[5,8,3,2,4,8,3],[7,4,8,4,8,3,4]], 36)])


def test(n, map, expected):
    answer = solution(n, map)
    assert answer == expected


def solution(n, map):
    INF = float("inf")
    mean_distance = [[INF] * n for _ in range(n)]
    mean_distance[0][0] = map[0][0]

    queue = []
    queue.append((map[0][0],0,0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        dist, x,y = queue.pop(0)

        if mean_distance[y][x] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (nx < 0 or nx >= n or ny < 0 or ny >= n):
                nd = dist + map[ny][nx]
                if nd < mean_distance[ny][nx]:
                    mean_distance[ny][nx] = nd
                    queue.append((nd, nx, ny))

    return mean_distance[n-1][n-1]