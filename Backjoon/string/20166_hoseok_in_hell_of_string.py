# 문자열 지옥에 떨어진 호석

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]

sub_string = {}

def DFS(y, x, god_string, board, depth):
    cnt = 0
    sub_pos = []
    N = len(board)
    M = len(board[0])
    depth += 1
    if depth >= len(god_string):
        return 1

    nxt_alphabet = god_string[depth]


    for i in range(8):
        ny = (y + dy[i]) % N
        nx = (x + dx[i]) % M
        board_nxt_alphabet = board[ny][nx]
        if board_nxt_alphabet == nxt_alphabet:
            if depth == len(god_string) - 1:
                cnt += 1
            else:
                cnt += DFS(ny, nx, god_string, board, depth)
            sub_pos.append((ny, nx))

    temp = god_string[:depth+1]
    if temp in sub_string:
        sub_string[temp] += sub_pos
    else:
        sub_string[temp] = sub_pos

    return cnt


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = []
    for _ in range(N):
        row = input()
        board.append(row)

    for _ in range(K):
        god_string = input()
        cnt = 0
        depth = 0

        for d in range(1, K):
            if god_string[:d+1] in sub_string:
                depth = d

        if depth == 0:
            for i in range(N):
                for j in range(M):
                    if board[i][j] == god_string[depth]:
                        cnt += DFS(i, j, god_string, board, depth)
        else:
            for pos in sub_string[god_string[:depth+1]]:
                cnt += DFS(pos[0], pos[1], god_string, board, depth)

        print(cnt)