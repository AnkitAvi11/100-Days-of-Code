
#   function to print the permutation of a string
def permutation(string, counter, result, level) :
    if level == len(string) : 
        print('Permutation = ', result)
        return

    for i in range(len(string)) : 
        if counter[i] == 1 : 
            result[level] = string[i]
            counter[i] = 0
            permutation(string, counter, result, level+1)
            counter[i] = 1


#   driver code
def main() : 
    
    string = input()
    counter = [1] * len(string)
    result = [0] * len(string)
    permutation(string, counter, result, 0)

if __name__ == '__main__' : 
    main()