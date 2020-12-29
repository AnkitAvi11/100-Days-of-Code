"""
Find pair with given sum in the array
"""

#   using sorting (nlogn)
def find_pairs(arr : list, target : int) : 
    arr.sort()
    result = list()
    left = 0;right = len(arr) - 1

    while left < right : 
        csum = arr[left] + arr[right]

        if csum == target : 
            result.append([arr[left], arr[right]])
            left+=1;right-=1

        elif csum < target : 
            left += 1
        else : 
            right -= 1

    return result


#   drive code
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    target = 5

    print(find_pairs(arr, target))

