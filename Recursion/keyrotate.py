def binary_search(arr, lb, ub, sk) : 
    mid = (lb+ub) // 2
    if lb > ub : 
        return -1

    if arr[mid] == sk : 
        return mid
    elif sk > arr[mid] : 
        return binary_search(arr, mid+1, ub, sk)
    elif sk < arr[mid] : 
        return binary_search(arr, lb, mid-1, sk)

def main() : 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = list(map(int, input().split()))
        sk = int(input())
    
        pos = -1
        for i in range(n-1) : 
            if arr[i] > arr[i+1] : 
                
                pos = i
                break

        index = -1
        index = binary_search(arr, 0, pos, sk)
        if index == -1 : 
            index = binary_search(arr, pos+1, n-1, sk)

        print(index)


if __name__ == '__main__' : 
    main()