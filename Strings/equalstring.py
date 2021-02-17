#   function to rotate an array by 1
def rotate_arr(arr : list) : 
    arr.append(arr[0])
    arr.pop(0)

#   function to get the minimum number of moves
def min_moves(arr : list) -> int : 
    min_so_far = float("inf")
    for i in range(len(arr)) : 
        count = 0
        for j in range(len(arr)) : 
            if i != j : 
                if arr[i] == arr[j] : continue
                temp = list(arr[i])
                
                for _ in range(len(temp)) : 
                    if ''.join(temp) == arr[j] : 
                        break
                    else : 
                        rotate_arr(temp)
                        count+=1
                
        if count == 0 : 
            return -1

        min_so_far = min(min_so_far, count)

    return min_so_far if min_so_far !=0 else -1

#   main function
def main() : 
    #   input 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = list()
        for _ in range(n) : 
            arr.append(input())

        #   calling of the min_moves functions
        print(min_moves(arr))

#   driver code
if __name__ == '__main__' : 
    main()