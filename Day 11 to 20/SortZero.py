"""
Program to sort an array of 0, 1 and 2 without using extra space and sorting algorithm

"""

def sortzero(arr : list) -> None : 

    left = 0;mid = 0
    right = len(arr) - 1

    while mid <= right : 

        el = arr[mid]

        if el == 0 : 
            arr[left], arr[mid] = arr[mid], arr[left]
            left+=1
            mid+=1
        
        elif el == 1 : 
            mid+=1

        else : 
            #   element = 2
            arr[mid], arr[right] = arr[right], arr[mid]
            right-=1

if __name__ == "__main__":
    arr = [1,2,1,0,0,1,2,1,0]
    sortzero(arr)
    print(arr)