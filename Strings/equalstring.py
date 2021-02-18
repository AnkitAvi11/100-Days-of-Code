"""
Equal Strings
-------------
You are given N strings, You have to make all the strings equal if possible.

Output : Print the minimum number of moves required to make all the strings equal or -1 if it is not possible to make them equal at all
"""

#   function to get the minimum number of moves
def min_moves(arr : list) -> int : 
    arr.sort()
    
    min_moves = 99999
    
    for i in range(len(arr)) : 
        count = 0 
        for j in range(len(arr)) : 
            if i!=j and arr[i] != arr[j] : 
                temp = arr[j] + arr[j]
                if temp.count(arr[i]) > 0 : 
                    count += temp.index(arr[i])
                else: 
                    return -1
        min_moves = min(min_moves, count)

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