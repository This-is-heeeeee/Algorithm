def post_to_in(post) :
    infix = ""
    fisrst_operator = ['*', '/']
    second_operator = ['+', '-']
    temp = []
    for i in post:
        if i >= 'A' and i <= 'Z':
            infix = infix + i
        elif i in fisrst_operator:
            while temp:
                if temp[-1] not in fisrst_operator:
                    break
                else :
                    infix = infix + temp.pop(-1)
            temp.append(i)
        elif i in second_operator:
            while temp:
                if temp[-1] == '(':
                    break
                else :
                    infix = infix + temp.pop(-1)
            temp.append(i)
        elif i == '(':
            temp.append(i)
        else :
            while True:
                if temp[-1] == '(':
                    temp.pop(-1)
                    break
                else :
                    infix = infix + temp.pop(-1)

    while temp :
        infix = infix + temp.pop(-1)

    return infix

def main() :
    post = input()
    print(post_to_in(post))

if __name__ == "__main__" :
    main()