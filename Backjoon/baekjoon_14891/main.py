gears = [[]*8 for _ in range(4)]
def rotate(n, d):
    queue = []
    queue.append(n)
    dp = [0, 0, 0, 0]

    while queue :
        num = queue[0]
        if num-1 >=0:
            if dp[num-1] == 0 and gears[num][6] != gears[num-1][2] :
                queue.append(num-1)
        if num+1 <= 3:
            if dp[num+1] == 0 and gears[num][2] != gears[num+1][6] :
                queue.append(num+1)

        if (n-num)%2 == 0 :
            direction = d
        else :
            direction = d*-1

        if direction == 1 :
            temp = gears[num].pop(7)
            gears[num].insert(0, temp)
        else :
            temp = gears[num].pop(0)
            gears[num].insert(7, temp)
        queue.pop(0)
        dp[num] = 1

    return

def calc() :
    sum = 0
    for i in range(4) :
        sum = sum + gears[i][0] * (2 ** i)

    return sum
def main() :
    for i in range(4) :
        gear = int(input())
        for _ in range(8):
            gears[i].insert(0,int(gear%10))
            gear = gear/10

    K = int(input())
    for i in range(K) :
        n, d = map(int, input().split())
        rotate(n-1, d)
        #print(gears)

    print(calc())

if __name__ == "__main__" :
    main()
