# 미로 최단 루트
import pytest
from collections import deque

@pytest.mark.parametrize("N,M,data,expected",
                         [(5,6,
                           ['101010',
                            '111111',
                            '000001',
                            '111111',
                            '111111'],10)])
def test(N,M,data,expected):
    result = solve(N,M,data)
    assert result == expected

def solve(N,M,data):
    maze = [[int(data[i][j]) for j in range(M)] for i in range(N)]     # str list을 2차원 int list로 초기화
    queue = deque()

    maze[0][0] = 2
    queue.append((0,0))
    count = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while True:
        q_temp = deque()                                    # 다음 레벨의 노드들을 저장할 queue
        count += 1                                          # 다음 레벨에 도착 할 때마다 count
        while queue :                                       # 지금 레벨에서 저장된 노드를 모두 돌면 탈출
            x, y = queue.popleft()
            if (x, y) == (N-1, M-1) :
                return count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx in range(N) and ny in range(M) and maze[nx][ny] == 1:
                    q_temp.append((nx,ny))
        queue = q_temp

# 레벨마다 노드를 저장할 queue를 구분하여 풀어서 굳이 queue로 구현할 필요는 없었을듯

def solve_book(N,M,data):
    maze = [[int(data[i][j]) for j in range(M)] for i in range(N)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx not in range(N) or not ny in range(M):
                continue
            if maze[nx][ny] == 0:                           # 어차피 노드의 값이 1일때만 push하므로 굳이 검사 할 필요 없어 보임
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[N-1][M-1]

# 매 노드 첫 방문마다 count값을 update해줘 N,M자리의 값이 최소 방문 횟수
# 모든 노드를 방문해야 끝남
