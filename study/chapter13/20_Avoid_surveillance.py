# 감시 피하기

import pytest


@pytest.mark.parametrize("n,map,expected",
                         [(5, [["X", "S", "X", "X", "T"],
                               ["T", "X", "S", "X", "X"],
                               ["X", "X", "X", "X", "X"],
                               ["X", "T", "X", "X", "X"],
                               ["X", "X", "T", "X", "X"]], "YES"),
                          (4, [["S", "S", "S", "T"],
                               ["X", "X", "X", "X"],
                               ["X", "X", "X", "X"],
                               ["T", "T", "T", "X"]], "NO")])

def test(n,map,expected):
    answer = solution(n, map)
    assert answer == expected


def solution(n, map):
    T_list = []
    S_list = []
    for i in range(n):
        for j in range(n):
            if map[i][j] == "T":
                T_list.append([i,j])
            elif map[i][j] == "S":
                S_list.append([i,j])

    #find line
    surveillance_line = []
    for T in T_list:
        tx, ty = T
        for S in S_list:
            sx, sy = S
            tmp_line = []
            if tx == sx:
                if ty <= sy:
                    step = 1
                else:
                    step = -1
                for y in range(ty, sy, step):
                    tmp_line.append((tx, y))
            elif ty == sy:
                if tx <= sx:
                    step = 1
                else:
                    step = -1
                for x in range(tx, sx, step):
                    tmp_line.append((x, ty))
            if tmp_line:
                if len(tmp_line) == 1:
                    return "NO"
                surveillance_line.append(tmp_line)

    specific = []
    for i in range(len(surveillance_line)-1):
        for j in range(i+1,len(surveillance_line)):
            and_list = list(set(surveillance_line[i][1:]).intersection(surveillance_line[j]))
            if and_list:
                break
        else:
            specific.append(surveillance_line[i])
    specific.append(surveillance_line[-1])

    #print(surveillance_line)
    #print(specific)

    if len(specific) <= 3:
        return "YES"

    return "NO"
"""
if __name__ == "__main__":
    n = int(input())
    map = []
    for i in range(n):
        m = list(input().split())
        map.append(m)

    print(solution(n,map))
"""