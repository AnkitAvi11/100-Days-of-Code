def is_palindrome(string) : 
    left = 0 
    right = len(string) - 1

    while left <= right : 
        if string[left] != string[right] : return False
        left += 1;right -= 1

    return True

def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        print(is_palindrome(string))


if __name__ == '__main__' : 
    main()