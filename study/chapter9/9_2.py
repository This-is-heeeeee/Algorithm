# 전보
# 일방통행
# C에서부터 전보를 보낼 수 있는 나라의 수와 최대 시간
# 플로이드워셜
import pytest

INF = int(1e9)

@pytest.mark.parametrize("N,M,C,nodes,expected",
                         [(3,2,1,[[1,2,4],[1,3,2]], (2,4))])
def test(N,M,C,nodes,expected):
    answer = solve(N,M,C,nodes)
    assert answer == expected

def solve(N,M,C,nodes):
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for node in nodes:
        graph[node[0]][node[1]] = node[2]

    for i in range(1,N+1):
        graph[i][i] = 0

    for i in range(1,N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])

    count = N - graph[C].count(INF)

    max = 0
    for dist in graph[C]:
        if dist > max and dist < INF:
            max = dist

    return count, max
