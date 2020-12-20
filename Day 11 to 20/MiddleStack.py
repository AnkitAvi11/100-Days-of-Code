"""
Design a stack with operations on middle element
1. push() which adds an element to the top of the stack
2. pop() which removes an element from the top of the stack
3. findMiddle() which return the middle element of the stack
4. deleteMiddle() which deleted the middle element of the stack
"""

class Stack : 

    def __init__(self) : 
        self.arr = list()


    def push(self, sk) : 
        self.arr.append(sk)

    def pop(self) : 
        self.arr.pop()


    def findMiddle(self) : 
        if self.arr : 
            if len(self.arr) <= 2 : 
                return self.arr[0]
            return self.arr[len(self.arr) // 2]
        else : 
            return -1


    def deleteMiddle(self) : 
        if self.arr : 
            if len(self.arr) <= 2 : 
                return self.arr.pop(0)
            return self.arr[len(self.arr) // 2]

        else : 
            return -1

#   driver code
if __name__ == "__main__":
    pass