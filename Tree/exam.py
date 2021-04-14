
#   function to validate the cipher text and the string
def checkStrings(string, cipher) : 
    chars = [0] * 26

    for el in string : 
        chars[(ord(el) - 60)%26] += 1

    for el in cipher : 
        chars[ord(el) - 65] -= 1
    
    for el in chars : 
        if el > 0 : 
            return "No"
    
    return "Yes"
    

#   main function of the program
def main() :
    string = input().upper()
    cipher = input().upper()
    
    print(checkStrings(string, cipher))

    
#   driver code of the program
if __name__ == '__main__' : 
    main()

