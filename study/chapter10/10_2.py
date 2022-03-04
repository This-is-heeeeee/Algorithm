# 도시 분할 계획
# 크루스칼
import pytest

@pytest.mark.parametrize("N,M,edges,expected",
                         [(7,12,[[1,2,3],
                                 [1,3,2],
                                 [3,2,1],
                                 [2,5,2],
                                 [3,4,4],
                                 [7,3,6],
                                 [5,1,5],
                                 [1,6,2],
                                 [6,4,1],
                                 [6,5,3],
                                 [4,5,3],
                                 [6,7,4]], 8)])
def test(N,M,edges,expected):
    answer = solve(N,M,edges)
    assert answer == expected

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve(N,M,edges):
    answer = 0
    parent = [n for n in range(0, N + 1)]

    for edge in edges:
        edge[0], edge[2] = edge[2], edge[0]

    print(edges)
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            last = cost


    return answer - last
