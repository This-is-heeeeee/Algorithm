import copy
graph = []
df = []

def bfs(p1, p2):
    queue = []
    queue.append(p1)

    while queue:
        p = queue.pop(0)
        if p == p2:
            continue
        for i in range(len(graph)):
            if graph[p][i] != 0:
                if p == p1:
                    queue.append(i)
                    continue
                dist = df[p1][p] + graph[p][i]
                if df[p1][i] > 0 and df[p1][i] <= dist:
                    continue
                df[p1][i] = dist
                df[i][p1] = dist
                queue.append(i)

def main():
    global graph, df
    N, E = map(int, input().split())

    graph = [[0] * (N+1) for _ in range(N+1)]

    for i in range(E) :
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    df = copy.deepcopy(graph)

    v1, v2 = map(int, input().split())

    bfs(1, v1)
    bfs(1, v2)
    bfs(v1, v2)
    bfs(v1, N)
    bfs(v2, N)

    way_1 = df[1][v1] + df[v1][v2] + df[v2][N]
    way_2 = df[1][v2] + df[v1][v2] + df[v1][N]

    if df[1][v1] == 0 or df[v2][N] == 0:
        way_1 = 0

    if df[1][v2] == 0 or df[v1][N] == 0:
        way_2 = 0

    if df[v1][v2] == 0 or (not way_1 and not way_2):
        dist = -1

    elif way_1 and not way_2:
        dist = way_1

    elif way_2 and not way_1:
        dist = way_2

    else:
        dist = way_1 if way_1 < way_2 else way_2

    print(dist)

if __name__ == "__main__":
    main()