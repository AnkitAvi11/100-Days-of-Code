def rotate(string) : 
    string = list(string) 
    string.append(string[0])
    string.pop(0)
    return ''.join(string)


def check_is_rotation(string1, string2) : 
    if len(string1) != len(string2) : return False
    for _ in range(len(string1)) : 
        if string1 == string2 : 
            return True
        string1 = rotate(string1)
    return False


def main() : 
    string1 = input()
    string2 = input()

    print(check_is_rotation(string1, string2))

if __name__ == '__main__' : 
    main()