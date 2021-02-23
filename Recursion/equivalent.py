
def is_equaivalent(string1, string2) : 
    if string1 == string2 : 
        return True

    mid = len(string1) // 2

    if mid == 0 : 
        return False

    a1, a2 = string1[:mid], string1[mid:]
    b1, b2 = string2[:mid], string2[mid:]

    if (is_equaivalent(a1, b1) and is_equaivalent(a2, b2) or (is_equaivalent(a2, b1) and is_equaivalent(a1, b2))) : 
        return True

    return False
   

def main() : 
    string1 = input()
    string2 = input()

    if len(string1) != len(string2) : 
        print("NO")
        return

    if is_equaivalent(string1, string2) : 
        print("YES")
    else : 
        print("NO")


if __name__ == '__main__' : 
    main()