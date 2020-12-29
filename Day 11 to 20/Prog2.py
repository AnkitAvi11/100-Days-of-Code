"""
Program to check if the sub array with sum = 0 exists or not
"""

def check_sub_array(arr) : 
    s = set()
    
    s.add(0)

    sum_so_far = 0

    for el in arr : 
        sum_so_far += el

        if sum_so_far in s : 
            return True
        
        s.add(sum_so_far)

    return False

if __name__ == "__main__":
    a = [1,2,3]

    print(check_sub_array(a))