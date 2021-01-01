"""
python program to move all the negative elements to one side of the array
-------------------------------------------------------------------------

In this, the sequence of the array does not matter. 
Time complexity : O(n)
space complexity : O(1)

"""


#   function to move negatives to the right of the array
def move_negative(arr : list) -> None : 
    left = 0;right = len(arr) - 1
    
    while left < right : 
        if arr[left] < 0 : 
            while arr[right] < 0 : right-=1
            #   swap the two ends of the array
            arr[left], arr[right] = arr[right], arr[left]   
            left += 1
            right -= 1
        else : 
            left += 1


#   driver code
if __name__ == "__main__":
    arr = [1,2,-1,3,5,-2,7,8]
    move_negative(arr)
    print(arr)