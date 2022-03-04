# 커리큘럼
# 위상정렬
import pytest
from collections import deque

@pytest.mark.parametrize("N,lectures,expected",
                         [(5,[[10,-1],
                              [10,1,-1],
                              [4,1,-1],
                              [4,3,1,-1],
                              [3,3,-1]], [10,20,14,18,17])])
def test(N,lectures,expected):
    answer = solve(N,lectures)
    assert answer == expected

def solve(N,lectures):
    indegree = [0] * (N + 1)
    graph = [[] for i in range(N + 1)]

    for b in range(1, N+1):
        for a in lectures[b-1][1:-1]:
            graph[a].append(b)
            indegree[b] += 1

    time = [lecture[0] for lecture in lectures]
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        max = 0
        for t in lectures[now-1][1:-1]:
            if time[t - 1] > max:
                max = time[t - 1]

        time[now - 1] += max

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    return time
