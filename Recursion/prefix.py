
def prefix(arr) : 
    for i in range(1, len(arr)) : 
        if arr[:i+1].count(1) >= arr[:i+1].count(0) : 
            continue
        else : 
            return False

    return True


def find_prefix(arr, i) : 
    if i == len(arr) : 
        if prefix(arr) : 
            print(arr)
        return

    arr[i] = 1
    find_prefix(arr, i+1)
    arr[i] = 0
    find_prefix(arr, i+1)

def main() : 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = [0] * n
        arr[0] = 1
        find_prefix(arr, 1)

if __name__ == '__main__' : 
    main()