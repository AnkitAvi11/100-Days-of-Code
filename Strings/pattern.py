def checK_pattern(string : str) -> bool : 
    flag = True

    if len(string) < 3 : 
        return True
    
    first = int(string[0])
    second = int(string[1])

    cstring = str(first)+str(second)

    while len(cstring) < len(string) : 
        summation = first + second
        first = second
        second = summation
        cstring += str(summation)

    print(cstring, string)

    if cstring == string : 
        return True

    return False

def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        if checK_pattern(string) : 
            print("Yes")
        else : 
            print("No")

if __name__ == '__main__' : 
    main()