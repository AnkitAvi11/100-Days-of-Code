"""

Implementing a stack using a single queue
-----------------------------------------
This method can be very costly in terms of time complexity. 
We need to reverse the queue everytime we push an element into the stack.

"""


class Stack : 

    def __init__(self) : 
        self.queue = list()     #   queue to implement stack

    
    #   function to push an element into the stack
    def push(self, sk) : 
        self.queue.append(sk)

        for i in range(len(self.queue)) : 
            x = self.queue.pop(0)
            self.queue.append(x)


    #   function to pop an element from the stack
    def pop(self) : 
        if self.queue : 
            return self.queue.pop(0)

        return -1
