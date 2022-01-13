N=0
M=0
df = []
count = 0
ind_i = [-1,0,1,0]
ind_j = [0,1,0,-1]
stop = False

def func(r,c,d):
    global df,count, back, stop
    if df[r][c] == 0 :
        count = count+1
        df[r][c] = 2

    elif df[r][c] == 1:
        return

    for _ in range(4):
        if stop :
            return
        d = (d + 3)%4
        if df[r+ind_i[d]][c+ind_j[d]] == 0 :
            func(r+ind_i[d], c+ind_j[d], d)

    d_back = (d+2)%4
    if df[r+ind_i[d_back]][c+ind_j[d_back]] == 1:
        stop = True
        return

    func(r+ind_i[d_back], c+ind_j[d_back], d)


def main() :
    global N, M, df
    N, M = map(int, input().split())
    df = [[0]*M for _ in range(N)]
    r, c, d = map(int, input().split())
    for i in range(N):
        walls = list(map(int, input().split()))
        for j in range(len(walls)):
            df[i][j] = walls[j]
    func(r,c,d)
    #print(df)
    print(count)

if __name__ == "__main__" :
    main()