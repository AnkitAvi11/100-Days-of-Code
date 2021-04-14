#   class for the Node of the tree
class Node : 
    def __init__(self, data) -> None : 
        self.data = data
        self.left = None
        self.right = None


#   class for the tree operations
class Tree : 
    def __init__(self) -> None : 
        self.__root = None


    #   function to get the root
    def getRoot(self) : 
        return self.__root

    
    #   function to insert nodes in the tree
    def insertNode(self, data) : 
        new_node = Node(data)
        if self.__root is None : 
            self.__root = new_node
        else : 
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

    
    #   function to print the in order traversal using recursion
    def inOrder(self, root) : 
        if root is not None : 
            self.inOrder(root.left)
            print(root.data, end = " ")
            self.inOrder(root.right)

    
    #   function to print the in order without recursion
    def inOrderWithoutRecursion(self) : 
        stack = list()
        curr = self.__root

        while True : 
            if curr is not None : 
                stack.append(curr)
                curr = curr.left
            elif stack : 
                temp = stack.pop()
                print(temp.data, end = " ")
                curr = temp.right
            else : 
                break


    #   helper function to delete the node (DeepestRightNode is deleted here)
    def deleteHelper(self, keynode) : 
        queue = list()
        queue.append(self.__root)

        while queue : 
            temp = queue.pop(0)
            if temp is keynode : 
                temp = None
                return 
            
            if temp.left and temp.left is keynode : 
                temp.left = None
                return
            else : 
                queue.append(temp.left)
            
            if temp.right and temp.right is keynode : 
                temp.right = None
                return
            else : 
                queue.append(temp.right)
    
    
    #   function to delete the Node from the tree (get the node to be deleted)
    def deleteNode(self, root, key) : 
        
        #   when the tree has no elements
        if root is None : return "No node to be deleted"
        #   when the tree has only one element (node)
        if root.left is None and root.right is None : 
            if root.data == key : 
                root = None
                return "Node deleted"
            else : 
                return "No node to be deleted"
        
        #   when the tree has more than one nodes
        queue = list()
        queue.append(root)
        key_node = None

        while queue : 
            temp = queue.pop(0)

            if temp.data == key : 
                key_node = temp
            
            if temp.left : 
                queue.append(temp.left)
            
            if temp.right : 
                queue.append(temp.right)

        if key_node is not None : 
            data = temp.data
            self.deleteHelper(temp)
            key_node.data = data
            return "Node was deleted succesfully"
        
        return "No node to be deleted"


    #   function to count the height of the tree
    def countHeight(self, root) : 
        if root is None : return 0
        left = 1 + self.countHeight(root.left)
        right = 1 + self.countHeight(root.right)
        return max(left, right)

    
    #   function to print the left view helper
    def leftViewHelper(self, root, level, maxlevel) : 
        if root is None : return None
        if maxlevel[0] < level : 
            print(root.data, end = " ")
            maxlevel[0] = level
        
        self.leftViewHelper(root.left, level+1, maxlevel)
        self.leftViewHelper(root.right, level+1, maxlevel)


    #   leftview function (function for the same that calls the helper function)
    def leftView(self, root) : 
        maxlevel = [0]
        self.leftViewHelper(root, 1, maxlevel)

    
    #   function to print each path of the tree
    def printEachPath(self, root, stack) : 
        if root is None : return
        stack.append(root.data)
        if root.left is None and root.right is None : 
            print(stack)
        
        self.printEachPath(root.left, stack)
        self.printEachPath(root.right, stack)
        stack.pop()

    
    #   function to get the sum of tree
    def getSum(self, root) : 
        if root is None : return 0
        return root.data + self.getSum(root.left) + self.getSum(root.right)


    #   function to check of checksumTree
    def checkSumTree(self, root) : 
        if root is None or (root.left is None and root.right is None) : 
            return True
        
        leftSum = self.getSum(root.left)
        rightSum = self.getSum(root.right)

        if root.data == leftSum + rightSum and self.checkSumTree(root.left) and self.checkSumTree(root.right) : 
            return True
        
        return False



#   main function of the program
def main() : 
    tree = Tree()
    tree.insertNode(1)
    tree.insertNode(2)
    tree.insertNode(3)
    tree.insertNode(4)
    tree.insertNode(5)
    tree.insertNode(6)
    tree.insertNode(7)

    tree.inOrder(tree.getRoot())
    print()
    tree.inOrderWithoutRecursion()
    print()
    print("Tree height = ", tree.countHeight(tree.getRoot()))
    tree.leftView(tree.getRoot())
    tree.printEachPath(tree.getRoot(), [])


#   driver code for the program
if __name__ == '__main__' : 
    main()

