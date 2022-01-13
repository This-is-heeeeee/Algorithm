ind = [[],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
space = []
fish = []
shark = []
# 0 : 빈칸, -1 : 상어
def rotate(f):
    for _ in range(8):
        next_r = f[0] + ind[f[2]][0]
        next_c = f[1] + ind[f[2]][1]
        try :
            if next_c >= 0 and next_r >= 0:
                if space[next_r][next_c] != -1:
                    return True, f
        except IndexError as e:
            pass
        f[2] = f[2]% 8 + 1

    return False, f

def move_fish():
    for f in fish:
        if f[2] == -1:   #먹힌 물고기
            continue

        check, f = rotate(f)

        if check:
            next_r = f[0] + ind[f[2]][0]
            next_c = f[1] + ind[f[2]][1]
            if space[next_r][next_c] == 0:
                space[next_r][next_c] = space[f[0]][f[1]]
                space[f[0]][f[1]] = 0
                f[0] = next_r
                f[1] = next_c
            else :
                temp = space[next_r][next_c]
                space[next_r][next_c] = space[f[0]][f[1]]
                space[f[0]][f[1]] = temp
                fish[temp][0] = f[0]
                fish[temp][1] = f[1]
                f[0] = next_r
                f[1] = next_c

def eating():
    for _ in range(3):
        if
    return

def main() :
    global space, fish, shark
    space = [[0]*4 for _ in range(4)]
    fish = [[-1]*3 for _ in range(17)]
    for i in range(4):
        f = list(map(int, input().split()))
        for j in range(0,8,2):
            space[i][int(j/2)] = f[j]
            fish[f[j]] = [i, int(j/2), f[j+1]]

    first = space[0][0]
    shark = [0,0,fish[first][2]]
    fish[first][2] = -1
    space[0][0] = -1

    print(space)
    move_fish()
    print(space)

if __name__ == "__main__" :
    main()