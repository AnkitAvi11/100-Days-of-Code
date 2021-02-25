
def main() : 
    n, k = map(int, input().split())

    time_limit = 240 - k 

    arr = [i*5 for i in range(1, n+1)]

    max_problems = 0;count = 0

    for el in arr : 
        if max_problems + el <= time_limit : 
            max_problems = max_problems + el
            count += 1

    print(count)


main()