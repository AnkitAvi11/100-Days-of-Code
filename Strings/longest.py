
def count_substring_length(string : str) -> int : 
    seen = dict()
    last_index = 0

    max_len = 0

    for i in range(len(string)) : 
        if string[i] in seen : 
            last_index = max(last_index, seen[string[i]] + 1)

        seen[string[i]] = i
        max_len = max(max_len, i - last_index + 1)

    return max_len


def main() : 
    t = int(input())
    for _ in range(t) : 
        string = input()
        print(count_substring_length(string))


if __name__ == '__main__' :
    main()

