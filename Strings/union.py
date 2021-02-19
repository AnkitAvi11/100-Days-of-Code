#   program to find the union of two sorted arrays
class Solution : 
    def find_union(self, arr1, arr2) : 
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2) : 
            if arr1[i] < arr2[j] : 
                print(arr1[i], end = " ")
                i+=1
            elif arr2[j] < arr1[i] : 
                print(arr2[j], end = " ")
                j += 1
            elif arr1[i] == arr2[j] : 
                print(arr1[i], end = " ")
                i += 1
                j += 1
        
        if i == len(arr1) : 
            for el in arr2[j:] : 
                print(el, end = " ")
        else : 
            for el in arr1[i:] : 
                print(el, end = " ")


def main() : 
    t = int(input())
    for _ in range(t) : 
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        solution = Solution()

        solution.find_union(arr1, arr2)


if __name__ == '__main__' : 
    main()