
def print_pattern(count, n) : 
    print(count, end = "")
    if count >= n : 
        return
    print_pattern(count+1, n)
    print(count, end = "")

if __name__ == '__main__' :
    n = int(input()) 
    for i in range(1, n+1) : 
        print_pattern(1, i)
        print()