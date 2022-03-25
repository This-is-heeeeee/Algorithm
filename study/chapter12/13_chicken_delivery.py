# 치킨 배달
# 백준 테스트x
import pytest


@pytest.mark.parametrize("n,m,map,expected",
                         [(5, 3, [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]],5),
                          (5, 2, [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]],10),
                          (5, 1, [[1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]],11),
                          (5, 1, [[1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1]],32)])
def test(n, m, map, expected):
    answer = solution(n, m, map)
    assert answer == expected


def solution(n, m, map):
    answer = 0
    houses = []
    chickens = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                houses.append([i, j])
            elif map[i][j] == 2:
                chickens.append([i, j])

    chicken_from_house = [[0]*len(chickens) for _ in range(len(houses))]

    for i, house in enumerate(houses):
        for j, chicken in enumerate(chickens):
            dist = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
            chicken_from_house[i][j] = dist

    loop_len = len(chickens) - m
    for _ in range(len(chickens) - m):
        min_dist, remove_idx = 10000000, 0
        for idx in range(len(chickens)):
            temp = chicken_from_house.copy()
            for j, cfh in enumerate(chicken_from_house):
                temp[j] = cfh.copy()
                temp[j].remove(cfh[idx])
            chicken_dist_tmp = 0
            for i in range(len(temp)):
                chicken_dist_tmp = chicken_dist_tmp + min(temp[i])
            print(idx, chicken_dist_tmp)
            if chicken_dist_tmp <= min_dist:
                min_dist, remove_idx = chicken_dist_tmp, idx

        chickens.remove(chickens[remove_idx])
        for cfh in chicken_from_house:
            cfh.remove(cfh[remove_idx])

    chicken_dist = 0
    for i in range(len(chicken_from_house)):
        chicken_dist = chicken_dist + min(chicken_from_house[i])

    return chicken_dist