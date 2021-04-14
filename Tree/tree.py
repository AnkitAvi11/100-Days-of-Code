class TreeNode : 
    def __init__(self, data) : 
        self.data = data
        self.left = None
        self.right = None
    

class Tree : 
    def __init__(self) : 
        self.root = None
    
    #   function to get the root
    def getRoot(self) : 
        return self.root
    
    #   function to insert a node into the tree
    def createTree(self, data) : 
        new_node = TreeNode(data)
        if self.root is None : 
            self.root = new_node
        else : 
            queue = list()

            queue.append(self.root)

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

    
    #   function to print the inorder of the tree
    def inOrderTraversal(self, root) : 
        if root is not None : 
            self.inOrderTraversal(root.left)
            print(root.data, end = " ")
            self.inOrderTraversal(root.right)


    #   function for the pre-order traversal
    def preOrderTraversal(self, root) :
        if root is not None : 
            print(root.data, end = " ")
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
    

    #   function for the post order traversal
    def postOrderTraversal(self, root) : 
        if root is not None : 
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data, end = " ")

    
    #   function for in order traversal without recursion
    def inorder_without_recursion(self) : 
        stack = list()
        curr = self.root 

        while True : 
            if curr is not None : 
                stack.append(curr)
                curr = curr.left
            elif stack : 
                data_node = stack.pop()
                print(data_node.data, end = " ")
                curr = data_node.right
            else : 
                break
    
    #   function for the level order traversal of the binary tree
    def levelOrderTraversal(self) : 
        pass


#   main function for the program
def main() : 
    tree = Tree()
    tree.createTree(1)
    tree.createTree(2)
    tree.createTree(3)
    tree.createTree(4)
    tree.createTree(5)


    print("In order traversal")
    tree.inOrderTraversal(tree.root)
    print("\nPre order traversal")
    tree.preOrderTraversal(tree.root)
    print("\nPost order traversal")
    tree.postOrderTraversal(tree.root)

    print("\nInorder without recursion")
    tree.inorder_without_recursion()


#   driver code
if __name__ == '__main__' : 
    main()

