# 8x8평면 행:1~8 열:a~h
# 체스의 나이트의 현재 위치가 주어졌을때 이동가능한 경우의 수
import pytest

@pytest.mark.parametrize("position,expected",[('a1',2),('c2',6)])
def test(position, expected):
    result = solve(position)
    assert result == expected


def solve(position):
    x, y = ord(position[0])-ord('a')+1, int(position[1])
    dx = [-2,-2,2,2,-1,1,-1,1]
    dy = [-1,1,-1,1,-2,-2,2,2]
    count = 0
    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x in range(1,9) and next_y in range(1,9):
            count += 1

    return count

def solve_book(position):
    row = int(position[1])
    column = int(ord(position[0])) - int(ord('a')) + 1
    steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
            result += 1

    return result