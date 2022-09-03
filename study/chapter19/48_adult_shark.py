# 어른상어
# 백준 19237

# 1. 1000번 루프
# 2. 냄새 남기기.
# 3. 이동
# 4. 겹치면 제거


def solution(N, M, _map, sharks, priorities, K):
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    smell_map = [[[-1, 0]]*N for _ in range(N)]

    for _ in range(1001):
        #print(_map)
        if len(sharks) <= 1:
            return _
        for smell_row in smell_map:
            for smell in smell_row:
                if smell[0] != -1:
                    smell[1] -= 1
                    if smell[1] <= 0:
                        smell[0] = -1
        #print(sharks)
        for i in sharks:
            inf = sharks[i]
            smell_map[inf[0]][inf[1]] = [i, K]

        for i in range(M-1, -1, -1):
            if i not in sharks:
                continue
            inf = sharks[i]
            c_point = inf[0:2]
            for j in range(4):
                p = priorities[i][inf[2]][j]
                _next = [c_point[0] + d_row[p], c_point[1] + d_col[p]]

                if (_next[0] in range(N) and _next[1] in range(N)) and smell_map[_next[0]][_next[1]][0] == -1:
                    _map[inf[0]][inf[1]] = -1
                    _map[_next[0]][_next[1]] = i
                    sharks[i] = [_next[0],_next[1],p]
                    break
            else:
                for j in range(4):
                    p = priorities[i][inf[2]][j]
                    _next = [c_point[0] + d_row[p], c_point[1] + d_col[p]]

                    if (_next[0] in range(N) and _next[1] in range(N)) and smell_map[_next[0]][_next[1]][0] == i:
                        _map[inf[0]][inf[1]] = -1
                        _map[_next[0]][_next[1]] = i
                        sharks[i] = [_next[0], _next[1], p]
                        break

        for i in range(M - 1, -1, -1):
            if i not in sharks:
                continue
            inf = sharks[i]
            if _map[inf[0]][inf[1]] != i:
                del sharks[i]

    return -1



if __name__ == "__main__":
    N, M, K = list(map(int, input().split()))
    _map= []
    sharks = {i : [] for i in range(0,M)}
    priorities = {i : [] for i in range(0,M)}

    for i in range(N):
        row = list(map(int, input().split()))

        row_temp = []
        for c in row:
            row_temp.append(c - 1)

        row = row_temp

        for j in range(len(row)):
            if row[j] != -1:
                sharks[row[j]].append(i)
                sharks[row[j]].append(j)

        _map.append(row)

    directions = list(map(int, input().split()))

    for i in range(len(directions)):
        sharks[i].append(directions[i]-1)

    for i in range(M*4):
        priority = list(map(int, input().split()))
        temp = []
        for p in priority:
            temp.append(p-1)

        priorities[i//4].append(temp)


    print(solution(N, M, _map, sharks, priorities, K))
