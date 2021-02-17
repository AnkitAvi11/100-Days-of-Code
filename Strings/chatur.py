"""
Program to count the minimum number of operations required to convert a given string into a palindrome
"""

#   function to count the number of moves to convert a string into a palindrome
def count_moves(string : str) -> int : 
    count = 0
    left = 0; right = len(string) - 1
    while left <= right : 
        if string[left] == string[right] : 
            left += 1
            right -= 1
            continue
        count += abs(ord(string[left]) - ord(string[right]))
        left += 1
        right -= 1
    return count

#   main function
def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()

        print(count_moves(string))

#   driver code
if __name__ == '__main__' : 
    main()