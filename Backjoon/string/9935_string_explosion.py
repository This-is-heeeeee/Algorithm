# 문자열 폭발

#1. temp_stack : 폭발 문자열인지 확인하기 위한 스택
#2. 한 글자씩 비교하며 result와 temp_stack에 추가하고, 폭발 문자열이 완성되면 양쪽 스택에서 pop
#3. 폭발 문자열이 중간에 끊겼을경우 temp_stack 초기화


def solution(S, bomb):
    string = S
    len_bomb = len(bomb)
    result = []
    temp_stack = []

    last = -1
    for s in string:
        result.append(s)

        if s == bomb[0] or (len_bomb > 1 and s == bomb[last+1]):
            temp_stack.append(s)
            if s == bomb[0]:
                last = 0
            else:
                last = last + 1
            if last == len_bomb - 1:
                for _ in range(len_bomb):
                    result.pop(-1)
                    temp_stack.pop(-1)
                if temp_stack:
                    last = bomb.find(temp_stack[-1])
                else:
                    last = -1

        else:
            temp_stack = []
            last = -1

    if result:
        return ''.join(result)
    else:
        return 'FRULA'

if __name__ == "__main__":
    S = input()
    bomb = input()

    print(solution(S, bomb))
