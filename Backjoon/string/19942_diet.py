# 다이어트

from itertools import combinations

def solution(N, mpfsv, ingredients):
    sub_sets = []
    indices = [_ for _ in range(N)]
    for i in range(1, N+1):
        sub_sets += [list(j) for j in combinations(indices, i)]

    min_price = 500 * N
    min_sets = []

    for sub_set in sub_sets:
        p,f,s,v = 0,0,0,0
        price = 0
        for i in sub_set:
            if price > min_price:
                break
            p += ingredients[i][0]
            f += ingredients[i][1]
            s += ingredients[i][2]
            v += ingredients[i][3]
            price += ingredients[i][-1]

        if price > min_price:
            continue
        if p >= mpfsv[0]:
            if f >= mpfsv[1]:
                if s >= mpfsv[2]:
                    if v >= mpfsv[3]:
                        if price == min_price:
                            min_sets.append(sub_set)
                        else:
                            min_sets = [sub_set]
                        min_price = price

    #print(min_sets)
    if min_sets:
        print(min_price)
        min_sets.sort()
        min_set = [i + 1 for i in min_sets[0]]
        print(*min_set)
    else:
        print(-1)
    return


if __name__ == "__main__":
    N = int(input())
    mpfsv = list(map(int, input().split()))
    ingredients = []
    for _ in range(N):
        ingredient = list(map(int, input().split()))
        ingredients.append(ingredient)

    solution(N, mpfsv, ingredients)
