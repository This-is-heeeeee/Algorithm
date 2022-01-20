#NxM사이즈 맵/ 맵의 각 칸(A,B) - A행 B열/0:땅, 1:바다
#1. 현재 위치에서 왼쪽에 가보지 않은 칸이 있다면 왼쪽으로 회전 후 해당 칸으로 이동
#2. 없다면 회번 후 1번 재시행
#3. 갈 수 있는 곳이 없다면 방향은 그대로 놓고 후진, 후진 못할 시(바다일 때) break
import pytest

@pytest.mark.parametrize("map_size,character,maps,expected",[
    ([4,4],[1,1,0],
     [[1,1,1,1],
      [1,0,0,1],
      [1,1,0,1],
      [1,1,1,1]],3),
    ([3,3],[1,1,0],
     [[1,1,1],
      [1,0,1],
      [1,1,1]],1),
    ([11,10],[7,4,0],
     [[1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,1,1,1,1,0,1],
      [1,0,0,1,1,0,0,0,0,1],
      [1,0,1,1,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,1,0,1],
      [1,0,0,0,0,0,1,1,0,1],
      [1,0,0,0,0,0,1,1,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1]],57)])
def test(map_size,character,maps,expected):
    result = solve(map_size,character,maps)
    assert result == expected

def check_side(x,y,map_size):
    return True if x in range(map_size[1]) and y in range(map_size[0]) else False

def move(character, maps, map_size):
    left = [(0, -1), (-1, 0), (0, 1), (1, 0)]   # 바라보는 방향(0,1,2,3)에 따른 왼쪽 좌표
    back = [(1, 0), (0, -1), (-1, 0), (0, 1)]   # 바라보는 방향에 따른 뒤쪽 좌표
    x, y = character[1], character[0]
    for _ in range(4):
        left_x, left_y = x + left[character[-1]][1], y + left[character[-1]][0]
        if check_side(left_x, left_y, map_size) and maps[left_y][left_x] == 0:      # 왼칸이 맵 안에 있는지, 바다인지 땅인지 체크
            character = [left_y, left_x, (character[-1] + 3) % 4]                   # 왼쪽으로 이동
            maps[left_y][left_x] = 2                                                # 맵에 표시
            return character, maps, False
        character[-1] = (character[-1] + 3) % 4                                     # 왼쪽으로 이동할 수 없다면 회전만 하고 반복

    back_x, back_y = x + back[character[-1]][1], y + back[character[-1]][0]         # 갈 곳이 없을때 후진 할 좌표
    if check_side(back_x, back_y, map_size) and maps[back_y][back_x] != 1:          # 뒤칸 체크
        character = [back_y, back_x, character[-1]]                                 # 뒤로 이동
        return character, maps, False

    return character, maps, True                                                    # 이동할 수 없다면 끝

def solve(map_size, character, maps):
    end = False
    maps[character[0]][character[1]] = 2

    while not end:
        character, maps, end = move(character, maps, map_size)

    return sum(row.count(2) for row in maps)