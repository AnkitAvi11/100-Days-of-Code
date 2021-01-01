#   program to find the duplicate in an array of N+1 integers

def find_duplicate(arr : list) -> None : 
    slow = arr[0];fast = arr[0]

    slow = arr[slow]
    fast = arr[arr[fast]]

    while slow != fast : 
        slow = arr[slow]
        fast = arr[arr[fast]]

    fast = arr[0]

    while slow != fast : 
        slow = arr[slow]
        fast = arr[fast]

    return slow


if __name__ == "__main__":
    arr = [1,3,4,2,2]
    print(find_duplicate(arr))
