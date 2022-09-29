# 문자열 폭발


#1. 한 글자씩 비교하며 각각 스택에.


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
