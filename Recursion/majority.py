from collections import Counter

def find_max(arr : list, mid : int) -> int : 
    counter = Counter(arr)
    
    voter_id = -1
    max_votes = -1

    for key, el in counter.items() : 
        if el > mid : 
            max_votes = max(max_votes, el)
            voter_id = key
    
    print(voter_id)

def main() : 
    t = int(input())
    for _ in range(t) : 
        n = int(input())
        arr = list(map(int, input().split()))
        threshold = n // 2
        find_max(arr, threshold)

if __name__ == '__main__' : 
    main()
