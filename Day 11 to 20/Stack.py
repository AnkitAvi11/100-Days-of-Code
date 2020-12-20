
#   Day 12 : Stack implementation in  python

class Stack : 

    #   constructor for the class
    def __init__(self, size : int) -> None : 
        self.size = size
        self.arr = [0] * size
        self.top = -1


    #   function to push an element into the stack
    def push(self, sk : int) -> None : 
        if self.top == self.size - 1 : 
            print("Stack overflow")
            return

        self.top +=1 
        self.arr[self.top] = sk

        print("Element pushed")



    #   function to pop an element from the stack
    def pop(self) -> int : 
        if self.top == -1 : 
            print('Stack underflow')
            return -1

        popelement = self.arr[self.top]
        self.top -= 1
        return popelement


    #   function to traverse the stack 
    def traverse(self) -> None : 
        for el in self.arr : 
            print(el, end = " ")



if __name__ == '__main__' : 
    pass
