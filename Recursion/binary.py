def generate_binary(arr, i, n) : 
    if i == n : 
        for el in arr : 
            print(el, end="")

        print()
        return

    if arr[i-1] == 0 : 
        arr[i] = 0 
        generate_binary(arr, i+1, n)
        arr[i] = 1
        generate_binary(arr, i+1, n)

    if arr[i-1] == 1 : 
        arr[i] = 0
        generate_binary(arr, i+1, n)


def main() : 
    t = int(input()) 
    for _ in range(t) : 
        n = int(input())
        result = [0] * n

        result[0] = 0

        generate_binary(result, 1, n)

        result[0] = 1

        generate_binary(result, 1, n)
        

if __name__ == '__main__' : 
    main()