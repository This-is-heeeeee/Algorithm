# 금광

import pytest


@pytest.mark.parametrize("n, m, mine, expected",
                         [(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7], 19),
                          (4, 4, [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2], 16)])

def test(n, m, mine, expected):
    answer = solution(n, m, mine)
    assert answer == expected


def solution(n, m, mine):
    idx = 0
    mine_2d = []
    for i in range(n):
        tmp = mine[idx: idx + m]
        mine_2d.append(tmp)
        idx += m

    for i in range(1, m):
        for j in range(n):
            temp = []
            if j - 1 >= 0:
                temp.append(mine_2d[j - 1][i - 1] + mine_2d[j][i])
            temp.append(mine_2d[j][i - 1] + mine_2d[j][i])
            if j + 1 < n:
                temp.append(mine_2d[j + 1][i - 1] + mine_2d[j][i])

            mine_2d[j][i] = max(temp)

    result = max(m[-1] for m in mine_2d)
    print(mine_2d)

    return result

#1 3 1 4    1 5 8 16
#2 2 4 1    2 7 11 14
#5 0 2 3    5 5 13 16
#0 6 1 2    0 11 12 15
#?????????????????????????