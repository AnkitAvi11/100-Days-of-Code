
def print_substring(string) : 
    snum = 0
    
    res = list()
    while snum < pow(2, len(string)) : 
        temp = list()
        for i in range(len(string)) : 
            if (snum&(1<<i))!=0 : 
                temp.append(string[i])
        
        res.append(temp)
        snum+=1
    res.sort()
    for i in range(1, len(res)) : 
        for el in res[i] : 
            print(el, end=" ")
        print()

def main () : 
    string = input()
    string = list(string)
    string.sort()
    string = ''.join(string)
    print_substring(string)
    

if __name__ == '__main__' : 
    main()
