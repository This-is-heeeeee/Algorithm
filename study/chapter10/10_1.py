# 팀 결성
# 서로소 집합
import pytest

@pytest.mark.parametrize("N,M,data,expected",
                         [(7,8,[[0,1,3],
                                [1,1,7],
                                [0,7,6],
                                [1,7,1],
                                [0,3,7],
                                [0,4,2],
                                [0,1,1],
                                [1,1,1]], ['No', 'No', 'Yes'])])
def test(N,M,data,expected):
    answer = solve(N,M,data)
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

def solve(N,M,data):
    answer = []
    parent = [n for n in range(0, N + 1)]
    for d in data:
        if d[0] == 0:
            union_parent(parent, d[1], d[2])
        else:
            if find_parent(parent, d[1]) == find_parent(parent, d[2]):
                answer.append('Yes')
            else:
                answer.append('No')

    return answer
