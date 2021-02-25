if __name__ == '__main__' : 
    t = int(input())
    for _ in range(t) : 
        n, b = map(int, input().split())
        arr = list(map(int, input().split()))
        
        count = 0

        i = 0
        while b > 0 and i < n : 
            if b - arr[i] < 0 : 
                i+=1
            else : 
                b -= arr[i]
                count += 1
                i+=1

        print(count)