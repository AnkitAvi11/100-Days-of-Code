#   Python program for queue

class Queue : 

    #   constructor for the class
    def __init__(self) : 
        self.arr = list()


    def hasElements(self) :
        if self.arr : 
            return True
        return False

    #   inserting an element 
    def insert(self, sk) : 
        self.arr.append(sk)

    #   popping out the first element
    def deleteElement(self) : 
        if self.arr : 
            return self.arr.pop(0)

        return -1

    
if __name__ == "__main__":
    pass