# 아기상어
# 백준 16236

#1. 주변 체크
#2. 남은 먹이 있는지 체크


def check_around(n, map, shark):
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    for i in range(4):
        ny = shark[0] + dy[i]
        nx = shark[1] + dx[i]

        if ny in range(n) and nx in range(n):
            if map[ny][nx] < shark[2] and map[ny][nx] != 0:
                shark[3] += 1
                if shark[3] == shark[2]:
                    shark[2] += 1
                    shark[3] = 0
                shark[0] = ny
                shark[1] = nx
                map[ny][nx] = 0
                return True

    return False

import copy

def find_next_fish(n, map, shark, before, count, _min):
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    y,x = shark[0:2]
    if map[y][x] < shark[2] and map[y][x] != 0:
        shark[3] += 1
        if shark[3] == shark[2]:
            shark[2] += 1
            shark[3] = 0
        map[y][x] = 0
        if count < _min[0]:
            _min[0] = count
            #print(_min)
        return map, shark, count

    temps = []

    before.append(shark[0:2])

    if count + 1 > _min[0]:
        return None

    for i in range(4):
        ny = shark[0] + dy[i]
        nx = shark[1] + dx[i]

        if ny in range(n) and nx in range(n):
            if [ny, nx] in before or map[ny][nx] > shark[2]:
                continue
            else:
                temps.append(find_next_fish(n, copy.deepcopy(map), [ny,nx,shark[2],shark[3]], copy.deepcopy(before), count+1, _min))

    temp_min = n*n
    min_idx = n
    for i, temp in enumerate(temps):
        if temp:
            if temp[2] < temp_min:
                temp_min = temp[2]
                min_idx = i
    #print(temps)
    if temp_min != n*n:
        #print("______")
        return temps[min_idx]


def solution(n, map, shark):
    count = 0
    while True:
        if not any(i in range(1,shark[2]) for row in map for i in row):
            return count
        if check_around(n, map, shark):
            count+=1
            #print(shark)
            continue
        else:
            temp = find_next_fish(n, map, shark, [], 0, [n*n])
            if temp:
                map, shark = temp[0:2]
                count += temp[2]
                #print(shark)
            else:
                #print(map)
                break

    return count

if __name__ == "__main__":

    n = int(input())
    ocean = []
    shark = None

    for _ in range(n):
        row = list(map(int, input().split()))

        if 9 in row:
            shark = [_, row.index(9),2,0]
            row[row.index(9)] = 0

        ocean.append(row)


    print(solution(n, ocean, shark))
