import copy
import sys
sys.setrecursionlimit(1000000)

A = []
out = 0
df = []
move_i = [-1,0,1,0] # front = direction, left = direction+1
move_j = [0,-1,0,1]
surr_ind = [[[],[],[-2,0],[],[]],
        [[],[-1,-1],[-1,0],[-1,1],[]],
        [[ 0,-2],[ 0,-1],[ 0,0],[ 0,1],[ 0,2]],
        [[],[ 1,-1],[ 1,0],[ 1,1],[]],
        [[],[],[ 2,0],[],[]]]

ratio = [[0, 0, 5, 0, 0],
         [0,10, 0,10, 0],
         [2, 7, 0, 7, 2],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0]]


def change_direction(direction):
    global ratio
    d = (direction+1) % 4

    n = 5

    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[n-j-1][i] = ratio[i][j]

    ratio = copy.deepcopy(result)

    return d


def check_left(r,c,direction):
    d = (direction+1) % 4
    if df[r+move_i[d]][c+move_j[d]] == 0:
        return True

    else :
        return False


def spread(r,c,d):
    global out
    n = 5
    total_spread = 0

    for i in range(n):
        for j in range(n):
            if ratio[i][j] == 0:
                continue
            sand = int(A[r][c] * ratio[i][j] / 100)
            total_spread = total_spread + sand

            r_ind = r+surr_ind[i][j][0]
            c_ind = c+surr_ind[i][j][1]
            if (r_ind < 0 or r_ind >= len(df)) or (c_ind < 0 or c_ind >= len(df)):
                out = out + sand
                continue
            A[r_ind][c_ind] = A[r_ind][c_ind] + sand

    a_r = r+move_i[d]
    a_c = c+move_j[d]
    sand = A[r][c]-total_spread
    if (a_r < 0 or a_r >= len(df)) or (a_c < 0 or a_c >= len(df)):
        out = out + sand
    else:
        A[a_r][a_c] = A[a_r][a_c] + (sand)
    A[r][c] = 0


def tornado(r,c,d):
    df[r][c] = 1

    if check_left(r,c,d):
        d = change_direction(d)

    next_r = r+move_i[d]
    next_c = c+move_j[d]
    if (next_c < 0 or next_c >= len(df)) or (next_r < 0 or next_r >= len(df)):
        return
    spread(next_r,next_c,d)
    tornado(next_r,next_c,d)


def main():
    global df
    N = int(input())
    df = [[0]*N for _ in range(N)]
    for i in range(N):
        a = list(map(int, input().split()))
        A.append(a)

    i = int(N/2)

    tornado(i, i, 0)

    print(out)


if __name__ == "__main__":
    main()