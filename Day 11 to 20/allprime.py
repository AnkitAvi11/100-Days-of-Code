import math

def isPrime(num) : 
    if num == 2 : return True
    for i in range(2, math.ceil(math.sqrt(num)) + 1) : 
        if num%i == 0 : 
            return False

    return True


if __name__ == "__main__":
    n = int(input("Enter a number : "))

    for i in range(2, n+1) : 
        if isPrime(i) : 
            print(i)

            