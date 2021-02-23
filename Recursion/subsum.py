def subArray(arr, n):

    snum = 0
    summation = 0 
    while snum < pow(2,n) :
        for i in range(n) : 
            if((snum&(1<<i))!=0) : 
                summation += arr[i]		
        snum+=1

    return summation
	

def main() : 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = list(map(int, input().split()))

        print(subArray(arr, n))
        

if __name__ == '__main__' : 
    main()
    