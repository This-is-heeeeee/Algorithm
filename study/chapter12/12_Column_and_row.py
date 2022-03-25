# 기둥과 보 설치
# remove_check에서 런타임 에러
import pytest

@pytest.mark.parametrize("n,build_frame,expected",
                         [(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]],[[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]),
                          (5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]], [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])])
def test(n,build_frame,expected):
    answer = solution(n,build_frame)
    assert answer == expected


def check(objs):
    for obj in objs:
        if obj[2] == 0:
            if not(obj[1] == 0 or [obj[0],obj[1]-1, 0] in objs or [obj[0]-1,obj[1], 1] in objs or [obj[0],obj[1],1] in objs):
                return False
        else:
            if not([obj[0],obj[1]-1, 0] in objs or [obj[0]+1,obj[1]-1, 0] in objs or ([obj[0]-1,obj[1], 1] in objs and [obj[0]+1,obj[1], 1] in objs)):
                return False

    return True


def solution(n, build_frame):
    answer = [[]]
    objs = []

    for bf in build_frame:
        if bf[-1] == 1:
            objs.append(bf[:-1])
            if not check(objs):
                objs.remove(bf[:-1])

        else:
            objs.remove(bf[:-1])
            if not check(objs):
                objs.append(bf[:-1])


    objs.sort(key=lambda x:(x[0],x[1],x[2]))
    answer = objs


    return answer