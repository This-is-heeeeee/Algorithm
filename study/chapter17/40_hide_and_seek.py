# 숨바꼭질


import pytest


@pytest.mark.parametrize("n, m, AB, expected",
                         [(6, 7, [(3, 6), (4, 3), (3, 2), (1, 3), (1, 2), (2, 4), (5, 2)], (4, 2, 3))])


def test(n, m, AB, expected):
    answer = solution(n, m, AB)
    assert answer == expected


def solution(n, m, AB):
    nodes = [[] for _ in range(n)]
    INF = float("inf")
    mean_distance = [INF for _ in range(n)]
    mean_distance[0] = 0

    for ab in AB:
        nodes[ab[0] - 1].append(ab[1] - 1)
        nodes[ab[1] - 1].append(ab[0] - 1)

    queue = []
    queue.append((0,0))

    while queue:
        dist, idx = queue.pop(0)

        if mean_distance[idx] < dist and mean_distance != 0:
            continue

        nd = dist + 1
        for next_node in nodes[idx]:
            if nd < mean_distance[next_node]:
                mean_distance[next_node] = nd
                queue.append((nd, next_node))

    for i in range(len(mean_distance)):
        if mean_distance[i] == INF:
            mean_distance[i] = 0

    max_dist = max(mean_distance)
    return (mean_distance.index(max_dist)+1, max_dist, mean_distance.count(max_dist))