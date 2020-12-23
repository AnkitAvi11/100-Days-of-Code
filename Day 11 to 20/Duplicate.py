#   Find the duplicate in an array of N+1 integers

def find_duplicate(arr : list) -> int : 
    slow = arr[0]; fast = arr[0]

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
    print(find_duplicate([2,5,9,6,9,3,8,9,7,1]))
