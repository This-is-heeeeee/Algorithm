# 성적 낮은 학생 순서 출력
import pytest

@pytest.mark.parametrize("N,data,expected",
                         [(3, {'홍길동': 95, '이순신': 77}, ['이순신', '홍길동'])])
def test(N, data, expected):
    result = solve(N,data)
    assert result == expected

def sorted_key(data):
    return data[1]

def solve(N, data):
    return list(dict(sorted(data.items(), key=lambda x : x[1])).keys())
