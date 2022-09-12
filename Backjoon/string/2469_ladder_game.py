# 사다리타기


#1. 위부터 ?까지 이동
#2. 아래부터 ?까지 이동
#3. 가능한지 확인


def solution(k, n, final, ladder):
    result = ['x' for _ in range(k-1)]
    upper_side = [0 for _ in range(k)]
    lower_side = [0 for _ in range(k)]
    Fail = 'x'*(k-1)

    for character in range(k):
        col = character
        for row in range(n):
            if ladder[row][0] == '?':
                upper_side[col] = character
                break
            if col==0:
                if ladder[row][col] == '*':
                    continue
                else:
                    col += 1
            elif col==k-1:
                if ladder[row][col-1] == '*':
                    continue
                else:
                    col -= 1
            else:
                if ladder[row][col-1] == '*':
                    if ladder[row][col] == '*':
                        continue
                    else:
                        col += 1
                else:
                    col -= 1
    #print(upper_side)

    for c in range(k):
        col = c
        character = final[c]
        for row in range(n-1, -1, -1):
            if ladder[row][0] == '?':
                lower_side[col] = character
                break
            if col==0:
                if ladder[row][col] == '*':
                    continue
                else:
                    col += 1
            elif col==k-1:
                if ladder[row][col-1] == '*':
                    continue
                else:
                    col -= 1
            else:
                if ladder[row][col-1] == '*':
                    if ladder[row][col] == '*':
                        continue
                    else:
                        col += 1
                else:
                    col -= 1
    #print(lower_side)

    for col in range(k):
        if col == 0:
            if upper_side[col] == lower_side[col]:
                result[col] = '*'
            elif upper_side[col] == lower_side[col+1]:
                result[col] = '-'
            else:
                return Fail
        elif col == k-1:
            if upper_side[col] == lower_side[col]:
                if result[col-1] != '*':
                    return Fail
            elif upper_side[col] == lower_side[col-1]:
                if result[col-1] != '-':
                    return Fail
            else:
                return Fail
        else:
            if upper_side[col] == lower_side[col]:
                result[col] = '*'
                if result[col-1] != '*':
                    return Fail
            elif upper_side[col] == lower_side[col+1]:
                result[col] = '-'
                if result[col-1] != '*':
                    return Fail
            elif upper_side[col] == lower_side[col-1]:
                result[col] = '*'
                if result[col-1] != '-':
                    return Fail

    return ''.join(result)



if __name__ == "__main__":
    k = int(input())
    n = int(input())

    final = input()
    final = [ord(character)-65 for character in final]
    ladder = []

    for _ in range(n):
        row = list(input())
        ladder.append(row)

    print(solution(k, n, final, ladder))
