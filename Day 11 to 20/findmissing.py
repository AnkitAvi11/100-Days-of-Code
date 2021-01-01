#   Find the missing number

def find_missing(arr : list) -> int : 
    has_seen = [0] * (len(arr) + 1)
    for el in arr : 
        has_seen[el-1] += 1

    for index, el in enumerate(has_seen) : 
        if el == 0 : return index+1

    return -1


if __name__ == "__main__":
    arr = [1,2,5,4,6,7]
    print(find_missing(arr))