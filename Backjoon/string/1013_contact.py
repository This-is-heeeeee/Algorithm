# contact
# 반례를 6시간동안 못찾았음.


def solution(signal, patterns):
    idx = 0
    p = 0
    count = [False, False, False]
    save_point = []
    while idx < len(signal):
        if p == 0:
            check = signal[idx:idx+2]
            if check in patterns[0]:
                idx += 2
                if check == patterns[0][0]:
                    p = 1
                else:
                    if not count[0]:
                        count[0] = True
            else:
                if save_point:
                    idx = save_point.pop(-1)
                    count = [True, False, False]
                    p = 0
                else:
                    return 'NO'

        elif p == 1:
            check = signal[idx]
            if check == patterns[1]:
                count[1] = True
                idx += 1
            elif check == patterns[2] and count[1]:
                count[1] = False
                p = 2
            else:
                if save_point:
                    idx = save_point.pop(-1)
                    count = [True, False, False]
                    p = 0
                else:
                    return 'NO'

        else:
            check = signal[idx]
            _next = signal[idx+1:idx+3]
            if check == patterns[2]:
                if not count[0]:
                    count[0] = True
                if idx == len(signal) - 1:
                    break
                count[2] = True
                idx += 1
                if _next == patterns[0][0]:
                    p = 0
                    count[2] = False
                    save_point.append(idx+1)
                elif _next == patterns[0][1]:
                    p = 0
            else:
                if save_point:
                    idx = save_point.pop(-1)
                    count = [True, False, False]
                    p = 0
                else:
                    return 'NO'

    if count[0:2] == [True,False]:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    test_case = int(input())

    patterns = [['10', '01'], '0', '1']
    #result = []
    for _ in range(test_case):
        signal = input()
        print(solution(signal, patterns))

        #result.append(solution(signal, patterns))

    #for r in result:
        #print(r)
