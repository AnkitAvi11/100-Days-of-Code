def is_valid(string, first, second) : 
    cstring = str(first) + str(second)

    while len(cstring) < len(string) :
        summation = first + second
        cstring = cstring + str(summation)
        first = second
        second = summation

    print(cstring, string)
    if cstring == string : 
        return True

    return False


def checK_pattern(string : str) -> bool : 
    for i in range(len(string)) : 
        first_num = int(string[:i+1])
        for j in range(i+1, len(string)) : 
            second_num = int(string[i+1:j+1])
            print("First num = ", first_num)
            print("Second num = ", second_num)
            summation = first_num + second_num
            
            first_string = str(first_num)+str(second_num)+str(summation)
            
            if string.startswith(first_string) :
                if is_valid(string, first_num, second_num) : 
                    return "Yes"

    return "No"

def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        print(checK_pattern(string))
        # if checK_pattern(string) : 
        #     print("Yes")
        # else : 
        #     print("No")

if __name__ == '__main__' : 
    main()