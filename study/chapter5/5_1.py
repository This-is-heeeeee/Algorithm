# NxM크기의 얼음 틀
# 1은 칸막이
# 생성되는 얼음 덩어리의 개수
import pytest

@pytest.mark.parametrize("N,M,data,expected",
                         [(4,5,
                           ['00110',
                            '00011',
                            '11111',
                            '00000'],3),
                          (15,14,
                           ['00000111100000',
                            '11111101111110',
                            '11011101101110',
                            '11011101100000',
                            '11011111111111',
                            '11011111111100',
                            '11000000011111',
                            '01111111111111',
                            '00000000011111',
                            '01111111111000',
                            '00011111111000',
                            '00000001111000',
                            '11111111110011',
                            '11100011111111',
                            '11100011111111'],8)])
def test(N,M,data,expected):
    result = solve(N,M,data)
    assert result == expected

def check(i, j, case):
    case[i][j] = 2
    if j+1<len(case[i]) and case[i][j+1] == 0:
        case = check(i,j+1,case)
    if i+1<len(case) and case[i+1][j] == 0:
        case = check(i+1,j,case)
    if j-1 > 0 and case[i][j-1] == 0:
        case = check(i,j-1,case)
    if i-1 > 0 and case[i-1][j] == 0:
        case = check(i-1,j,case)

    return case


def solve(N,M,data):
    case = [[int(data[i][j]) for j in range(M)] for i in range(N)]     # str list을 2차원 int list로 초기화
    count = 0

    for i in range(N):
        for j in range(M):
            if case[i][j] != 0:         # dfs를 돌기 전에 0인지(탐색의 필요성을) 체크
                continue
            #print(i,j)
            case = check(i,j,case)
            count += 1                  # 덩어리 하나 찾으면 count


    return count

"""
책이랑 다른점
1.
책 : dfs를 돌며 0인지 판단하고 0이었다면 True, 아니면 False(재귀함수 내에서는 사용되지 않는다)
나 : dfs를 돌기 전에 돌아야 하는지 판단, 돌고 나면 바뀐 그래프 return(전역번수가 아니기 때문에)
"""