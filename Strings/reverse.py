def reverse_string(string) : 
    string = list(string)
    left, right = 0, len(string) - 1

    while left <= right : 
        string[left], string[right] = string[right], string[left]
        left+=1;right-=1

    return ''.join(string)


def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        print(reverse_string(string))


if __name__ == '__main__' : 
    main()