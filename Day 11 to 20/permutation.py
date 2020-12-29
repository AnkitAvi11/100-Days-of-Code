
def permutation(string, counter, result, level) : 

    if level == len(string) : 
        print(result)
    
    else : 

        for i in range(len(string)) : 
            if counter[i] == 1 : 
                continue
            else : 
                result[level] = string[i]
                counter[i] = 1
                permutation(string, counter, result, level+1)
                counter[i] = 0
           


if __name__ == "__main__":

    counter = [0,0,0]
    result = [0,0,0]

    permutation('abc', counter, result, 0)

    