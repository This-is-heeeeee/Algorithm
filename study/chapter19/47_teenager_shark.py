# 청소년상어
# 백준 19236


#1. 물고기 이동 가능 확인
#2. 물고기 이동
#3. 상어 이동 가능 확인(물고기의 번호와 방향 확인 후 물고기 먹은 후의 상어의 이동이 가능한지 확인)
#4. 상어 이동
#5. DFS

import copy

def DFS(_map, fishes, shark, be_eaten):
    #print(_map)
    #print(shark)

    d_row = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    d_col = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    # 물고기 이동
    for n in range(1,17):
        if n not in fishes:
            continue
        temp = fishes[n][0:2]
        direction = fishes[n][2]

        for _ in range(8):
            _next = [temp[0] + d_row[direction], temp[1] + d_col[direction]]
            if (_next[0] in range(4) and _next[1] in range(4)) and _map[_next[0]][_next[1]] != -1:
                break
            direction = (((direction-1) + 1) % 8) + 1
        else:
            continue

        if _map[_next[0]][_next[1]] == 0:
            _map[_next[0]][_next[1]] = n
            _map[temp[0]][temp[1]] = 0
            fishes[n] = [_next[0],_next[1],direction]

        else:
            c_n = _map[_next[0]][_next[1]]
            c_direction = fishes[c_n][2]
            _map[_next[0]][_next[1]] = n
            _map[temp[0]][temp[1]] = c_n
            fishes[n] = [_next[0], _next[1], direction]
            fishes[c_n] = [temp[0], temp[1], c_direction]

    # 상어 이동
    direction = shark[2]
    temp = shark[0:2]
    result = []
    while temp[0] in range(4) and temp[1] in range(4):
        _next = _next = [temp[0] + d_row[direction], temp[1] + d_col[direction]]
        if (_next[0] in range(4) and _next[1] in range(4)) and _map[_next[0]][_next[1]] != 0:
            n = _map[_next[0]][_next[1]]
            temp_map = copy.deepcopy(_map)
            temp_fishes = copy.deepcopy(fishes)

            temp_map[shark[0]][shark[1]] = 0
            temp_shark = copy.deepcopy(fishes[n])
            del temp_fishes[n]
            temp_map[_next[0]][_next[1]] = -1

            result.append(DFS(temp_map, temp_fishes, temp_shark, be_eaten + n))
        temp = _next

    if not result:
        return be_eaten

    else:
        return max(result)


if __name__ == "__main__":

    _map = []
    shark = [0,0,0]
    be_eaten = 0

    fishes = {i : [0,0,0] for i in range(1,17)}

    for _ in range(4):
        row = list(map(int, input().split()))

        map_row = []
        for i in range(0,len(row),2):
            map_row.append(row[i])
            fishes[row[i]] = [_,i//2,row[i+1]]

        _map.append(map_row)

    fish_num = _map[0][0]
    be_eaten += fish_num
    shark[2] = fishes[fish_num][2]
    del fishes[fish_num]
    _map[0][0] = -1


    print(DFS(_map, fishes, shark, be_eaten))
