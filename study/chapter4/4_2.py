# 정수 N(0<=N<=23)이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지 3이 하나라도 포함되는 모든 경우의 수
import pytest

@pytest.mark.parametrize("N,expected",[(5,11475)])
def test(N, expected):
    result = solve(N)
    assert result == expected

def solve(N):
    probability_in_m_s = (5/6)*(9/10)*(5/6)*(9/10)    #분, 초 안에 3이 없을 확률
    probability_in_h = 1 if N < 3 else 1 - (int((N-3)/10)+1)/(N+1)    #시에 3이 없을 확률
    probability = 1 - probability_in_h*probability_in_m_s

    answer = (N+1)*3600*probability

    return answer

"""
    시에 3이 있는 가지 수
    3~12 : 1
    13~22 : 2
    23 : 3
    이기 때문에 N에서 3을 빼서 구간을 0~9, 10~19로 만들어 계산이 쉽도록 범위 조정
    조정 후
    0~9 : 1
    10~19 : 2
    20 : 3
"""

def solve_book(N):
    count = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    return count