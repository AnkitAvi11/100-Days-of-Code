def count_pairs(arr : list, n : int, target : int) -> int : 
    count = 0

    arr.sort()

    left, right = 0, len(arr) - 1

    while right < n : 
        diff = arr[right] - arr[left]
        if diff == target : 
            count += 1
            left +=1
            right += 1

        elif diff > target : 
            left += 1
        else : 
            right += 1

    return count


def main() : 
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(count_pairs(arr, n, k))


if __name__ == '__main__' : 
    main()