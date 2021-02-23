
def countSolutions(n, val): 
  
    # initialize total = 0  
    total = 0
  
    # Base Case if n = 1 and val >= 0 
    # then it should return 1 
    if n == 1 and val >=0: 
        return 1
  
    # iterate the loop till equal the val 
    for i in range(val+1): 
      
        # total solution of equations  
        # and again call the recursive  
        # function Solutions(variable,value) 
        total += countSolutions(n-1, val-i) 
  
    # return the total no possible solution  
    return total 


def main() : 
    t = int(input())
    for _ in range(t) : 
        n, z = map(int, input().split())

        print(countSolutions(n,z))
        

if __name__ == '__main__' : 
    main()