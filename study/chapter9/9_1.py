# 미래도시
# 모든 노드의 길이가 1일때 최단거리 1 -> K -> X
# 모든 노드의 길이가 일정하므로 BFS
import pytest

@pytest.mark.parametrize("N,M,nodes,X,K,expected",
                         [(5,7,[[1,2],
                            [1,3],
                            [1,4],
                            [2,4],
                            [3,4],
                            [3,5],
                            [4,5]], 4, 5, 3),
                          (4,2,[[1,3],
                                [2,4]], 3, 4, -1)])
def test(N,M,nodes,X,K,expected):
    answer = solve(N,M,nodes,X,K)
    assert answer == expected

def BFS(x, y, nodes):
    idx = []
    countnodes = [-1 for _ in range(len(nodes))]
    idx.append(x)
    countnodes[x] = 0
    while True:
        if not idx:
            return -1
        i = idx.pop(0)
        if i == y:
            break
        for next in nodes[i]:
            if countnodes[i] + 1 < countnodes[next] or countnodes[next] == -1:
                countnodes[next] = countnodes[i] + 1
                idx.append(next)

    return countnodes[y]

def solve(N,M,nodes,X,K):
    mynodes = [[] for _ in range(N+1)]
    for node in nodes:
        mynodes[node[0]].append(node[1])
        mynodes[node[1]].append(node[0])

    count_1_to_K = BFS(1,K,mynodes)
    count_K_to_X = BFS(K,X,mynodes)

    if count_1_to_K == -1 or count_K_to_X == -1:
        return -1

    return count_1_to_K + count_K_to_X
