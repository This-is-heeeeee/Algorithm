# 공유기 설치
import sys
import pytest


@pytest.mark.parametrize("n,c,X,expected",
                         [(5, 3, [1, 2, 8, 4, 9], 3)])


def test(n,c,X,expected):
    answer = solution(c,X)
    assert answer == expected


def solution(X, c):
    X.sort()

    low = 1
    high = X[-1] - X[0]
    answer = 0

    if c == 2:
        answer = high
        return answer

    while high >= low:
        count = 1
        mid = (high + low) // 2
        num = X[0]
        for x in X:
            if x >= num + mid:
                count += 1
                num = x

        if count >= c:
            low = mid + 1
            answer = mid
        elif count < c:
            high = mid - 1

    return answer

"""
if __name__ == "__main__":
    n, c = list(map(int, sys.stdin.readline().split()))
    X = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        X.append(x)

    print(solution(X, c))
"""