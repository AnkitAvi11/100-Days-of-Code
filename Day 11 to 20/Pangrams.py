
def pangrams(string : str) : 
    string = string.upper()
    alpha = [0]*26
    
    for el in string : 
        if el.isalpha() : alpha[ord(el) - 65] += 1

    return all(alpha) 


if __name__ == "__main__":
    print(pangrams("ankit"))