"""
def func1(K, w, v, total_w, total_v):
    total_w = total_w + w[0]
    total_v = total_v + v[0]

    if total_w > K :
        return 0, 0

    if len(w) == 1:
        return total_w, total_v

    wv1 = func1(K, w[1:], v[1:], total_w, total_v)
    wv2 = func2(K, w[1:], v[1:], total_w, total_v)

    if wv1[1] > wv2[1] :
        return wv1

    elif wv1[1] == wv2[1] :
        if wv1[0] < wv2[0] :
            return wv1[0]
        else :
            return wv2[0]

    else :
        return wv2

def func2(K, w, v, total_w, total_v):
    if len(w) == 1:
        return total_w, total_v

    wv1 = func1(K, w[1:], v[1:], total_w, total_v)
    wv2 = func2(K, w[1:], v[1:], total_w, total_v)

    if wv1[1] > wv2[1] :
        return wv1

    elif wv1[1] == wv2[1] :
        if wv1[0] < wv2[0] :
            return wv1[0]
        else :
            return wv2[0]

    else :
        return wv2

def func(K, w, v):
    wv1 = func1(K, w, v, 0, 0)
    wv2 = func2(K, w, v, 0, 0)

    if wv1[0] > K:
        return wv2[1]

    if wv1[1] > wv2[1] :
        return wv1[1]

    else :
        return wv2[1]

def main() :
    N, K = map(int, input().split())
    weight = []
    value = []
    for i in range(N) :
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    print(func(K, weight, value))

if __name__ == "__main__" :
    main()
"""
dp = []

def func(N, K, w, v):
    for i in range(N):
        if i == 0 :
            remain = K - w[i]
            dp[i][remain] = v[i]
            dp[i][K] = 0
        else :
            for j in range(K+1) :
                if dp[i-1][j] <= -1 :
                    continue
                else :
                    if dp[i][j] < dp[i-1][j] :
                        dp[i][j] = dp[i-1][j]

                    remain = j-w[i]
                    if remain <= -1 :
                        continue
                    else :
                        if dp[i][remain] < dp[i-1][j]+v[i]:
                            dp[i][remain] = dp[i-1][j]+v[i]


def main() :
    global dp
    N, K = map(int, input().split())
    weights = []
    values = []
    dp = [[-1]*(K+1) for _ in range(N)]
    for i in range(N) :
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)

    func(N, K, weights, values)
    max_value = max(map(max, dp))
    #print(dp)
    print(max_value)

if __name__ == "__main__" :
    main()