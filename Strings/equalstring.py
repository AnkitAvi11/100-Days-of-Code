#   function to rotate an array by 1
def rotate_arr(arr : list) : 
    arr.append(arr[0])
    arr.pop(0)

#   function to get the minimum number of moves
def min_moves(arr : list) -> int : 
    arr.sort()
    min_moves = 99999
    
    for i in range(len(arr)) :

        count = 0       
        flag = False
        for j in range(len(arr)) : 
            if i != j and arr[i] != arr[j]:               
                temp = list(arr[j])
                flag = False   
                for m in range(len(temp)) : 
                    
                    if ''.join(temp) == arr[i] : 
                        flag = True
                        
                        break
                    else : 
                        rotate_arr(temp)
                        count += 1

        if not flag : 
            return -1
        min_moves = min(min_moves, count)
    
    if not flag : 
        return -1

    return min_moves

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