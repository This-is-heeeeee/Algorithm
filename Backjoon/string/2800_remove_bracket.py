# 괄호제거

from itertools import combinations

def solution(func):
    the_number = func.count('(')

    brackets = []
    for i, x in enumerate(func):
        if x == '(':
            brackets.append([i, 0])
        elif x == ')':
            brackets.append([i, 1])

    bracket_sets = []
    open_idx = 0
    stack = []
    for x in brackets:
        if x[1] == 0:
            stack.append(open_idx)
            open_idx += 1
            bracket_sets.append([x[0], None])

        else:
            close_idx = stack.pop(-1)
            bracket_sets[close_idx][1] = x[0]

    sub_funcs = []
    sub_sets = []

    for i in range(1, len(bracket_sets)+1):
        sub_sets += [list(j) for j in combinations(bracket_sets, i)]

    for sub_set in sub_sets:
        remove_list = [idx for sub in sub_set for idx in sub]
        sub_func = ''
        for idx, x in enumerate(func):
            if idx not in remove_list:
                sub_func += x
        sub_funcs.append(sub_func)
    """
    for i in range(len(bracket_sets)):
        for j in range(i, len(bracket_sets)):
            sub_sets = bracket_sets[i:j+1]
            remove_list = [idx for sub in sub_sets for idx in sub]
            sub_func = ''
            for idx, x in enumerate(func):
                if idx not in remove_list:
                    sub_func += x
            sub_funcs.append(sub_func)
    """

    sub_funcs = list(set(sub_funcs))
    return sorted(sub_funcs)

if __name__ == "__main__":
    func = list(input())

    subs = solution(func)

    for s in subs:
        print(s)
