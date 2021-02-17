def rotate_string(string : list, i : int, j : int) -> None : 
    while i <= j : 
        string[i], string[j] = string[j], string[i]
        i+=1;j-=1

def main() : 
    t = int(input())
    for _ in range(t) : 
        original_string = input()
        fake_string = list(input())
        temp = fake_string.copy()
        rotate_string(fake_string, 0, 1)
        rotate_string(fake_string,2,len(fake_string)-1)
        rotate_string(fake_string, 0, len(fake_string)  - 1)

        if "".join(fake_string) == original_string :
            print("Yes")
        else : 
            rotate_string(temp, len(temp)-2, len(temp)-1)
            rotate_string(temp,0,len(fake_string)-3)
            rotate_string(temp, 0, len(fake_string)  - 1)
            if "".join(fake_string) == original_string :
              print("Yes")
            else : 
              print("No")

if __name__ == '__main__' : 
    main()