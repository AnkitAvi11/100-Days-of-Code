#   program to find the missing and repeating element in the list / array

def findMissingRepeating(arr : list) : 

    has_seen = set(arr)
    missing_number = -1;repeating_number = -1

    i = 1

    while True : 
        if i not in has_seen : 
            missing_number = i
            break

        i+=1

    has_seen = set()
    for el in arr : 
        if el in has_seen : 
            repeating_number = el;break
        has_seen.add(el)

    return (missing_number, repeating_number)



if __name__ == "__main__":
    print(findMissingRepeating([4,3,6,2,1,1]))
