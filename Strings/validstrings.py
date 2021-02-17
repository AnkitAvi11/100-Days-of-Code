def check_validity(string : str) -> bool : 
  stack = list()
  left_count = string.count('(')
  right_count = string.count(')')

  if left_count != right_count : 
    return False
  else : 
    for el in string : 
      if el == '(' : 
        stack.append(el)
      elif el == ')' and stack : stack.pop()

  if len(stack) <= 1 : 
    return True

  return False

def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        print(check_validity(string))

if __name__ == '__main__' : 
    main()