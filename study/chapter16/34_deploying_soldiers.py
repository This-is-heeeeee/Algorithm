# 병사 배치하기
#LIS(Longest Increasing Subsequence)

import pytest


@pytest.mark.parametrize("n, soldiers, expected",
                         [(7, [15, 11, 4, 8, 5, 2, 4], 2)])


def test(n, soldiers, expected):
    answer = solution(n, soldiers)
    assert answer == expected


def solution(n, soldiers):
    count = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if soldiers[j] > soldiers[i]:
                count[i] = max(count[i], count[j] + 1)

    result = n - max(count)

    return result

"""
if __name__ == "__main__":
    n = int(input())

    soldiers = list(map(int, input().split()))

    print(solution(n, soldiers))
"""