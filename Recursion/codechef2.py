def main() : 
    t = int(input())
    for _ in range(t) : 
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solved = list()
        for _ in range(n) : 
            solved.append(input())

        for el in solved : 
            marks = 0
            for i in range(len(el)) : 
                if int(el[i]) == 1 : 
                    marks += arr[i]

            print(marks)


if __name__ == '__main__' : 
    main()