def main() : 
  t = int(input())
  for _ in range(t) : 
    n = int(input())
    arr = list(map(int, input().split()))
    pos = n - 1
    if len(arr) == 1 : pos = 0
    else : 
      if arr[0] > arr[1] : pos = 0
      else : 
        for i in range(1, len(arr) - 1) : 
          if arr[i-1] < arr[i] > arr[i+1] : 
            pos = i
            break

    pos = min(pos, n - 1)
    print(pos)
    
main()