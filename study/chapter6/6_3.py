# 두 배열의 원소 교체
# 만들 수 있는 행렬 A의 최댓값 구하기
import pytest

@pytest.mark.parametrize("N,K,A, B,expected",
                         [(5, 3, [1, 2, 5, 4, 3], [5, 5, 6, 6, 5], 26)])
def test(N, K, A, B, expected):
    result = solve(N,K,A,B)
    assert result == expected

def solve(N, K, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(K):
        if A[i] >= B[i]:
            break
        A[i], B[i] = B[i], A[i]

    return sum(A)
