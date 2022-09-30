# 가르침
learned = 0
words = []


def DFS(K, start, learning):
    global learned
    result = 0

    if learning == K:
        for word in words:
            if word & learned == word:
                result += 1

        return result

    for i in range(start, 26):
        if learned & (1 << i) == 0:
            learned |= (1 << i)
            result = max(result, DFS(K, i + 1, learning + 1))
            learned &= ~(1 << i)

    return result


def main():
    global learned
    N, K = map(int, input().split())

    if K < 5:
        print(0)
        return
    elif K == 26:
        print(N)
        return

    learned |= (1 << (ord('a') - ord('a')))
    learned |= (1 << (ord('n') - ord('a')))
    learned |= (1 << (ord('t') - ord('a')))
    learned |= (1 << (ord('i') - ord('a')))
    learned |= (1 << (ord('c') - ord('a')))

    for i in range(N):
        string = input()

        temp = 0
        for char in string:
            temp |= (1 << (ord(char) - ord('a')))

        words.append(temp)

    print(DFS(K, 0, 5))


if __name__ == "__main__":
    main()

