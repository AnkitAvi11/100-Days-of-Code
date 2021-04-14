
#   function to check the array for the same
def checkArray(arr) : 
    summation = sum(arr)

    if summation % len(arr) != 0 : return -1

    ans = summation // len(arr)
    moves = 0

    for el in arr : 
        temp = el
        if temp < ans : 
            moves += (abs(ans-temp))
        else : 
            moves += (abs(ans-temp))

    return moves // 2


#   main function of the class
def main() : 
    arr = list(map(int, input().split()))
    arr.sort()
    #   calling the function
    print(checkArray(arr), end="")


#   driver code for the program
if __name__ == '__main__' : 
    main()


