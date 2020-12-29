#   Sort binary array in linear time
def sort_binary_array(arr) : 
    
    left = 0
    mid = 0

    while mid < len(arr) : 
        if arr[mid] == 0 : 
            arr[left], arr[mid] = arr[mid], arr[left]
            left+=1;mid+=1

        else : 
            mid+=1


if __name__ == "__main__":
    arr = [1,0,1,0,1,0,0,1]
    sort_binary_array(arr)
    print(arr)

