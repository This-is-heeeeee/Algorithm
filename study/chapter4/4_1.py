# NxN크기의 정사각형 맵
# 입력값 U D L R에 따라 상 하 좌 우로 한 칸씩 이동
# 가지 못하는 명령은 무시
# 도착 지점의 좌표
import pytest

@pytest.mark.parametrize("N,data,expected",[(5,['R','R','R','U','D','D'],[3,4])])
def test(N, data, expected):
    result = solve(N, data)
    assert result == expected


def solve(N, plans):
    traveler = [1, 1]

    move = {'L': [0,-1], 'R': [0,1],
            'U': [-1,0], 'D': [1,0]}

    for plan in plans:
        next = [traveler[0] + move[plan][0], traveler[1] + move[plan][1]]
        if next[0] not in range(1,N+1) or next[1] not in range(1,N+1):
            continue
        traveler = next

    return traveler

def solve_book(N, plans):
    x, y = 1, 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue

        x, y = nx, ny


    return [x,y]