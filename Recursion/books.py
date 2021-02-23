def main() : 
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  
  
  left_count, right_count = 0, 0
  left_sum, right_sum = 0, 0
  
  for el in arr : 
    left_sum  += el
    if left_sum >= k : 
      break
    left_count += 1
    
  for el in arr[::-1] : 
    right_sum += el
    if right_sum >= k : 
      break
    right_count += 1
    
  print(min(n-left_count, n-right_count))
  
main()