def generate_combinations(arr, result, i, index, n, k) : 
    
    if k == 0 : 
        print(result)
        return

    for j in range(i, n) : 
        result[index] = arr[j]
        generate_combinations(arr, result, j+1, index+1, n, k-1)           
    

def main() : 
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    result = [0] * k
    
    generate_combinations(arr, result, 0, 0, n, k)

if __name__ == '__main__' : 
    main()

