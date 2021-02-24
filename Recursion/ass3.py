def decode_message(string) : 
    res = list()

    for el in string : 
        next_char = chr(ord(el) - 3)
        if ord(el) - 3 < 65 : 
            next_char = chr(ord(el) - 3 + 26)
        res.append(next_char)

    return res   


if __name__ == '__main__' : 
    string = input()
    res = decode_message(string)
    res.reverse()
    print(''.join(res))