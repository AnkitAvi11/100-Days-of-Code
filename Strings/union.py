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
    arr = [1,2,3,4,5,8,9,10]
    arr2 = [4,5,6,7]
    solution = Solution()
    solution.find_union(arr, arr2)


main()