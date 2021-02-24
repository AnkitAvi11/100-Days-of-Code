def check_anagram(string1, string2) : 
    chars = [0] * 26
    string1 = string1.lower();string2 = string2.lower()
    
    for el in string1 : 
        if el.isalpha() : 
            chars[ord(el) - 97] += 1

    for el in string2 : 
        if el.isalpha() : 
            chars[ord(el) - 97] -= 1

    for char in chars : 
        if char != 0 : 
            return False

    return True


if __name__ == '__main__' : 
    string1 = input().strip()
    string2 = input().strip()

    if check_anagram(string1, string2) : 
        print("Yes")
    else : 
        print("No")