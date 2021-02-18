
def main() : 
    t = int(input())
    for _ in range(t) : 
        s = input()
        t = input()

        

        i, j = 0, 0
        flag = True

        while i < len(s) and j < len(t) : 
            if s[i] == t[j] : 
                i+=1;j+=1
            elif s[i] == '+' and t[j] == '-' : 
                flag = False;break
            elif s[i] == '-' and t[j] == '+' : 
                if s[i+1] == '-' : 
                    i+=2
                    j+=1
                else : 
                    flag = False
                    break
            
        
        if flag and (i==len(s) and j == len(t)): 
            print("YES")
        else : 
            print("NO")
            

if __name__ == '__main__' : 
    main()