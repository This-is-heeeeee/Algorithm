# 최종순위
# 50% 틀림
# 다시.

"""
import pytest


@pytest.mark.parametrize("n, t, m, ab, expected",
                         [(5, [5, 4, 3, 2, 1], 2, [[2, 4], [3, 4]], [5, 3, 2, 4, 1]),
                          (3, [2, 3, 1], 0, [], [2, 3, 1]),
                          (4, [1, 2, 3, 4], 3, [[1, 2], [3, 4], [2, 3]], 'IMPOSSIBLE')])


def test(n, t, m, ab, expected):
    answer = solution(n, t, m, ab)
    assert answer == expected
"""

def solution(n, t, m, ab):
    rank = [[] for _ in range(n)]

    T = []
    for i in t:
        for j in T:
            rank[j].append(i-1)
        T.append(i-1)

    for a,b in ab:
        if a-1 in rank[b-1]:
            rank[b-1].remove(a-1)
            rank[a-1].append(b-1)

        else:
            return 'IMPOSSIBLE'

    temp1 = [len(_) for _ in rank]
    temp2 = [_ for _ in range(n)]
    result_rank = [i+1 for _,i in sorted(zip(temp1,temp2), reverse=True)]

    _len = n-1
    for i in range(n):
        if temp1[result_rank[i]-1] < _len:
            return '?'
        _len -= 1

    return result_rank



if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        n = int(input())
        team = list(map(int, input().split()))
        m = int(input())

        ab = []

        for _ in range(m):
            temp = list(map(int, input().split()))
            ab.append(temp)

        result = solution(n, team, m, ab)

        if result == 'IMPOSSIBLE' or result == '?':
            print(result)

        else:
            print(*result)
