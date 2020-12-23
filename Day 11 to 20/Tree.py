#   class for creating a tree node
class Node : 
    def __init__(self, sk) : 
        self.data = sk
        self.left = None
        self.right = None


#   class for creating and representing a tree
class Tree : 

    #   constructor of the class
    def __init__(self) : 
        self.root = None    #   empty tree
    

    #   function to insert an element into the tree
    def insertNode(self, sk) : 
        new_node = Node(sk)

        #   if the tree has no leaves or nodes
        if self.root is None : 
            self.root = new_node

        else : 
            #   using a queue to keep track of the left and right node
            queue = list()
            queue.append(self.root)

            while queue : 
                temp = queue.pop(0)

                if temp.left is None : 
                    temp.left = Node(sk)
                    break
                else : 
                    queue.append(temp.left)

                if temp.right is None : 
                    temp.right = Node(sk)
                    break
                else : 
                    queue.append(temp.right)
