# 퇴사

import pytest


@pytest.mark.parametrize("n, tp, expected",
                         [(7, [[3, 10],[5, 20],[1, 10],[1, 20],[2, 15],[4, 40],[2, 200]], 45),
                          (10, [[1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[1, 7],[1, 8],[1, 9],[1, 10]], 55),
                          (10, [[5, 10],[5, 9],[5, 8],[5, 7],[5, 6],[5, 10],[5, 9],[5, 8],[5, 7],[5, 6]], 20),
                          (10, [[5, 50],[4, 40],[3, 30],[2, 20],[1, 10],[1, 10],[2, 20],[3, 30],[4, 40],[5, 50]], 90)])


def test(n, tp, expected):
    answer = solution(n, tp)
    assert answer == expected


def solution(n, tp):
    for i in range(n):
        next_idx = tp[i][0] + i
        if next_idx == n:
            if len(tp[i]) <= 2:
                tp[i].append(tp[i][1])
            continue
        elif next_idx > n:
            if len(tp[i]) <= 2:
               tp[i].append(0)
            else:
                tp[i][2] -= tp[i][1]
            continue

        for idx in range(next_idx, n):
            if len(tp[i]) <= 2:
                profit = tp[idx][1] + tp[i][1]
            else:
                profit = tp[idx][1] + tp[i][2]
            if len(tp[idx]) <= 2:
                tp[idx].append(profit)
            else:
                tp[idx][2] = max(tp[idx][2], profit)


    result = max(row[-1] for row in tp)

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