# 뱀
"""
import pytest

@pytest.mark.parametrize("N,K,apples,L,XC,expected",
                         [(6,3,[[3,4],[2,5],[5,3]],3,{3:'D',15:'L',17:'D'}, 9)])
def test(N,apples,XC,expected):
    answer = solve(N,K,apples,L,XC)
    assert answer == expected
"""

def collision_check(ny,nx, N, snake):
    if ny < 1 or ny > N or nx < 1 or nx > N:
        return False
    if (ny,nx) in snake:
        return False

    return True


def turn_check(d, XC, count):
    if count in XC:
        if XC[count] == 'D':
            d = (d + 1)%4
        else:
            d = (d + 3)%4

    return d


def solve(N,apples,XC):
    map = [[0] * (N+1) for _ in range(N+1)]

    d = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for apple in apples:
        map[apple[0]][apple[1]] = 1

    # 머리는 움직이고, 꼬리는 위치만 기억한 후 지우거나 남기거나만.

    snake = [(1,1)]
    count = 0

    while True:
        ny, nx = snake[-1][0] + dy[d], snake[-1][1] + dx[d]

        if collision_check(ny,nx, N, snake):
            snake.append((ny,nx))
            if map[ny][nx] == 1:
                map[ny][nx] = 0
            else:
                snake.pop(0)
        else:
            break
        count += 1
        d = turn_check(d, XC, count)

    return count + 1

def main():
    N = int(input())
    K = int(input())
    apples = []
    for _ in range(K):
        apple = list(map(int, input().split()))
        apples.append(apple)
    L = int(input())
    XC = {}
    for _ in range(L):
        X, C = input().split()
        XC[int(X)] = C
    print(solve(N,apples,XC))

if __name__ == "__main__":
    main()