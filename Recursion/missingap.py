def main() : 
  t = int(input())
  for _ in range(t) : 
    n = int(input())
    arr = list(map(int, input().split()))
    
    cd = dict()
    
    for i in range(1, n) : 
      if arr[i] - arr[i-1] in cd : cd[arr[i]-arr[i-1]] += 1
      else : cd[arr[i]-arr[i-1]] = 1

         
    cd = dict(sorted(cd.items(), key=lambda item : item[0]), reversed=True)
    
    
    actual_cd = list(cd.keys())[0]
        
    element = -1
    for i in range(1, len(arr)) : 
        if arr[i] - arr[i-1] != actual_cd : 
            element = arr[i-1] + actual_cd
            break

    print("Missing element = ", element)

if __name__ == '__main__' : 
    main()