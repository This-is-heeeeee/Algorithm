# A와 B


#1. T를 S로.
#2. S 뒤에 A를 추가 -> T 뒤에 A 삭제
#3. S를 뒤집고 뒤에 B를 추가 -> T 뒤에 B를 삭제 후 뒤집기


def action_1(T):
    T = T[:-1]
    return T
def action_2(T):
    T = T[:-1]
    T = T[::-1]
    return T
def solution(S, T):
    string = T
    while 1:
        if string[-1] == 'A':
            string = action_1(string)
        else :
            string = action_2(string)

        if len(string) == len(S):
            break

    if string == S:
        return 1

    return 0

if __name__ == "__main__":
    S = input()
    T = input()

    print(solution(S, T))
