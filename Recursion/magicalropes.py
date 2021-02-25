
def main() : 
    n, x, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    rate_of_growth = list(map(int, input().split()))

    min_days = 0
    low = 0
    high = 10**18

    while low <= high :
        mid = (low+high) // 2
        summation = 0;flag = False

        for i in range(n) : 
            if mid * rate_of_growth[i] + arr[i] >= k :
                summation += (mid*rate_of_growth[i] + arr[i])
                if summation >= x : 
                    flag = True
                    break


        if flag : 
            min_days = mid
            high = mid - 1
        else :
            low = mid + 1
            
    print(min_days)

if __name__ == '__main__' : 
    main()
