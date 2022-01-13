dp = []

def func(n, k) :
    if n == k :
        return 0

    queue = []
    queue.append(n)
    dp[n] = 0
    while queue :
        #print(queue)
        for j in range(len(queue)) :
            num = queue.pop(0)
            i = dp[num]
            if k > n :
                if num * 2 == k:
                    return i
                elif num*2 < k * 2 :
                    if dp[num * 2] <= -1:
                        queue.insert(0, num*2)
                        dp[num * 2] = i

            if num - 1 == k:
                return i + 1
            elif num-1 > -1 :
                if dp[num-1] <= -1 :
                    queue.append(num-1)
                    dp[num - 1] = i+1

            if num+1 == k :
                return i+1
            elif num+1 < k :
                if dp[num + 1] <= -1:
                    queue.append(num+1)
                    dp[num + 1] = i+1

def main() :
    global dp
    N, K = map(int, input().split())

    if K > N :
        dp = [-1]*(K * 2 + 1)
    else :
        dp = [-1] * (N * 2 + 1)

    print(func(N, K))

if __name__ == "__main__" :
    main()