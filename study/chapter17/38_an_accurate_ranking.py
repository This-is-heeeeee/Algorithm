# 정확한순위
# BFS

import pytest


@pytest.mark.parametrize("n, m, AB, expected",
                         [(6, 6, [(1, 5), (3, 4), (4, 2), (4, 6), (5, 2), (5, 4)], 1)])


def test(n, m, AB, expected):
    answer = solution(n, m, AB)
    assert answer == expected


def solution(n, m, AB):
    upper_nodes = [[] for _ in range(n)]
    lower_nodes = [[] for _ in range(n)]
    result = 0

    for ab in AB:
        upper_nodes[ab[0] - 1].append(ab[1] - 1)
        lower_nodes[ab[1] - 1].append(ab[0] - 1)

    print(upper_nodes)
    print(lower_nodes)

    for i in range(n):
        visited = [False for _ in range(n)]
        stack = []
        stack.append(i)
        count = -2
        while stack:
            idx = stack.pop(0)
            if not visited[idx]:
                count += 1
                visited[idx] = True
                for node in lower_nodes[idx]:
                    stack.append(node)

        visited[i] = False
        stack.append(i)
        while stack:
            idx = stack.pop(0)
            if not visited[idx]:
                count += 1
                visited[idx] = True
                for node in upper_nodes[idx]:
                    stack.append(node)
        print(count)
        if count == n - 1:
            result += 1

    return result