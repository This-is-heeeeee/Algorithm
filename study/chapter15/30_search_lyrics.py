# 가사 검색
# binary_search
# 효율성 2/5 성공

import pytest


@pytest.mark.parametrize("words,queries,expected",
                         [(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                           ["fro??", "????o", "fr???", "fro???", "pro?"],
                           [3, 2, 4, 1, 0])])

def test(words,queries,expected):
    answer = solution(words,queries)
    assert answer == expected

def comparison(word, query, low, high):
    mid = (high + low) // 2
    if high < low:
        return True

    if query[mid] != "?" and word[mid] != query[mid]:
        return False
    else :
        right = comparison(word, query, mid + 1, high)
        left = comparison(word, query, low, mid - 1)

        if right and left:
            return True
        else:
            return False


def solution(words,queries):
    answer = []
    for query in queries:
        count = 0
        for word in words:
            if len(query) == len(word):
                match = comparison(word, query, 0, len(query) - 1)

                if match:
                    count += 1
        answer.append(count)

    return answer