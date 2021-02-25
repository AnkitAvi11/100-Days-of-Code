
def main() : 
    t = int(input())
    for _ in range(t) : 
        m, h = map(int, input().split())
        bmi = m / (h ** 2)

        if bmi >= 30 : 
            print(4)
        elif 25 <= bmi <= 29 : 
            print(3)
        elif 19 <= bmi <= 24 : 
            print(2)
        else : 
            print(1)


if __name__ == '__main__' : 
    main()