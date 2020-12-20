"""
Design a stack that supports getMin() in O(1) time and O(1) extra space
"""

class Stack : 

    def __init__(self) : 
        self.arr = list()
        self.minimum = float("inf")

    def push(self, sk) : 
        if self.minimum > sk : 
            self.minimum = sk
        self.arr.append(sk)

    def pop(self) : 
        if self.arr : 
            return self.arr.pop()

        return -1

    def getMin(self) : 
        if self.arr : 
            return self.minimum

        return -1

    def traverse(self) : 
        for el in self.arr : 
            print(el, " ")


if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.getMin())

