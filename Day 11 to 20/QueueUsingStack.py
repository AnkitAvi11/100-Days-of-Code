
#   implementing queues using two stacks

class Queue : 

    def __init__(self) : 
        self.stack1 = list()    #   stack 1
        self.stack2 = list()    #   stack 2

    
    #   function to append an element into the queue
    def insert(self, sk) : 
        self.stack1.append(sk)


    #   function to perform pop the first element
    def delete(self) : 
        
        if not self.stack2 : 
            if self.stack1 : 
                while self.stack1 : self.stack2.append(self.stack1.pop())
            else : 
                return "Stack underflow"

        return self.stack2.pop()

