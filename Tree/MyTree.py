class Node : 
    def __init__(self, data) -> None : 
        self.data = data
        self.left = None
        self.right = None


class Tree : 

    #   constructor for the class
    def __init__(self) -> None : 
        self.__root = None

    
    """
    Function to insert a node into the tree
    """
    def insertNode(self, data) : 
        new_node = Node(data)
        if self.__root is None : 
            self.__root = new_node 
            return 
        
        queue = list()

        queue.append(self.__root)

        while queue : 
            temp = queue.pop(0)
            if temp.left is None : 
                temp.left = new_node 
                return
            else : 
                queue.append(temp.left)
            
            if temp.right is None : 
                temp.right = new_node
                return
            else : 
                queue.append(temp.right)
    

    #   function to perform in order traversal of the tree
    def inOrderTraversal(self, root) : 
        if root is not None : 
            self.inOrderTraversal(root.left)
            print(root.data, end = " ")
            self.inOrderTraversal(root.right)
    

    #   function to get the root
    def getRoot(self) : 
        return self.__root

    
    #   function for in order traversal without recursion
    def inorderWithoutRecursion(self) : 
        stack = list()
        curr = self.__root

        while True : 
            if curr is not None : 
                stack.append(curr)
                curr = curr.left
            elif stack : 
                temp = stack.pop()
                print(temp.data, end=" ")
                curr = temp.right
            else : 
                break

    
    #   function to delete the node found
    def deleteRightMostNode(self, key_node) : 
        queue = list()
        queue.append(self.__root)

        while queue : 
            temp = queue.pop(0)

            if temp is key_node : 
                temp = None
                return
            
            if temp.right is key_node : 
                temp.right = None
                return
            else : 
                queue.append(temp.right)
            
            if temp.left is key_node : 
                temp.left = None
                return
            else : 
                queue.append(temp.left)

    
    #   function to delete the node
    def deleteNode(self, key) : 
        if self.__root is None : return "Tree is empty"
        if self.__root.left is None and self.__root.right is None : 
            if self.__root.data == key : 
                temp = self.__root.data
                self.__root = None
                return temp
            else : 
                return "Element not found"
        
        queue = list()
        queue.append(self.__root)
        key_node = None

        while queue : 
            temp = queue.pop(0)

            if temp.data == key : 
                key_node = temp
            
            if temp.left is not None : 
                queue.append(temp.left)
            
            if temp.right is not None : 
                queue.append(temp.right)


        if key_node is None : 
            return "Element was not found"
        else : 
            data = temp.data
            self.deleteRightMostNode(temp)
            key_node.data = data

    
    """
    Function to count the height of the tree
    """
    def countHeight(self, root) : 
        if root is None : return 0
        left = 1 + self.countHeight(root.left) 
        right = 1 + self.countHeight(root.right)
        print(left, right)
        return max(left, right)


    """
    Helper function for the left view of the tree function
    """
    def viewUntil(self, root, level, maxlevel) : 
        if root is None : return
        
        if maxlevel[0] < level : 
            print(root.data, end = " ")
            maxlevel[0] = level
        
        self.viewUntil(root.left, level+1, maxlevel)
        self.viewUntil(root.right, level+1, maxlevel)


    """
    Function to print the left view of the tree
    """
    def leftView(self) : 
        maxlevel = [0]
        self.viewUntil(self.__root, 1, maxlevel)
        


    """
    Function to convert a normal tree into its mirror tree
    """
    def reverseTree(self, root) : 
        if root is None : 
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.reverseTree(root.left)
        self.reverseTree(root.right)


    """
    Function to find the level wise average
    """
    def levelWiseAverage(self) : 
        if self.__root is None : return "{.2f}".format(0)
        if self.__root.left is None and self.__root.right is None : 
            print("{:.2f}".format(self.__root.data))
            return

        res = list()
        res.append("{:.2f}".format(self.__root.data))
        queue = list()
        queue.append(self.__root)

        while queue : 
            temp = queue.pop(0)
            num = 0 
            if temp.left and temp.left.data!=-1 : 
                num += temp.left.data
                queue.append(temp.left)
            
            if temp.right and temp.right.data!=-1: 
                num += temp.right.data
                queue.append(temp.right)
            
            
            if temp.left and temp.right and temp.left.data!=-1 and temp.right.data!=-1: 
                res.append("{:.2f}".format(num/2))
            else : 
                res.append("{:.2f}".format(num))

        print(res)


def main() : 
    tree = Tree()
    tree.insertNode(9)
    tree.insertNode(7)
    tree.insertNode(5)
    tree.insertNode(2)
    tree.insertNode(-1)
    tree.insertNode(-1)
    tree.insertNode(-1)
    tree.insertNode(-1)
    tree.insertNode(3)
    tree.insertNode(-1)
    tree.insertNode(-1)   

    tree.levelWiseAverage()


if __name__ == '__main__' : 
    main()