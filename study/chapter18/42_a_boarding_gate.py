# 탑승구
# DFS

import pytest


@pytest.mark.parametrize("G,P, gi, expected",
                         [(4, 3, [4, 1, 1], 2),
                          (4, 6, [2, 2, 3, 3, 4, 4], 3)])


def test(G,P, gi, expected):
    answer = solution(G, P, gi)
    assert answer == expected

def DFS(current_plane, gi, available_gates, count):
    counts = []
    if current_plane >= len(gi):
        return count

    for i in range(gi[current_plane]):
        temp = available_gates.copy()
        if temp[i]:
            temp[i] = False
            counts.append(DFS(current_plane+1, gi, temp, count + 1))

    if counts:
        return max(counts)
    else:
        return count


def solution(G, P, gi):
    available_gates = [True for _ in range(G)]

    return DFS(0, gi, available_gates, 0)