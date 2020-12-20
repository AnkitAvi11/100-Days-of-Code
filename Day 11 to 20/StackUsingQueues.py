#   Day 22 : Stack using two queues

class Queue : 

    def __init__(self) : 
        self.arr = list()

    def insert(self, sk : int) -> None : 
        self.arr.append(sk)

    def delete(self) -> int : 
        if self.arr : 
            return self.arr.pop(0)
        return -1

    def haselements(self) : 
        if self.arr : return True
        return False

    def deletelast(self) : 
        if self.arr : 
            return self.arr.pop()

        return -1


class Stack : 

    def __init__(self) : 
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.cursor = -1


    #   method to insert element into the stack
    def push(self, sk) : 
        self.queue1.insert(sk)

    
    #   method to pop element from the stack
    def pop(self) : 
        if self.cursor == -1 : #    when the cursor is at -1
            if self.queue1 : 
                while self.queue1.haselements() : 
                    self.queue2.insert(self.queue1.delete())
                    self.cursor += 1
            else : 
                return -1   #   both the queues are empty (stack underflow)

        if self.queue2 : 
            element = self.queue2.deletelast()
            self.cursor -= 1
            return element
        else : 
            return -1


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.pop())

    stack.push(4)
    stack.push(5)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())