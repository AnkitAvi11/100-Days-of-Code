
def main() : 
  t = int(input())
  for _ in range(t) : 
    n = int(input())
    arr = list()
    for _ in range(n) : 
      arr.append(input())
    
    sum_so_far = 999999
    for i in range(n) : 
      flag = False
      for j in range(n) : 
        temp = list(arr[i]).copy()
        count = -1
        if i!=j : 
          if "".join(temp) == arr[j] : 
            break
          else : 
            for k in range(len(temp) - 1) : 
              temp.append(temp[0])
              temp.pop(0)
              count += 1
              if ''.join(temp) == arr[j] : 
                flag = True

      if not flag : 
        print(-1)
        break
      else : 
        sum_so_far = min(sum_so_far, count)

    if sum_so_far >= 0 : 
      print(sum_so_far)
    else :
      print(-1)

if __name__ == '__main__' : 
  main()