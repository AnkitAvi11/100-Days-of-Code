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
        self.nodes_count = 0
    

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

    
    #   function to get the root
    def get_root (self) : 
        return self.root

    #   pre order traversal of the tree
    def preOrderTraversal(self, root) : 
        if root is None : 
            return
        else : 
            print('Data = {}'.format(root.data))
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    
    #   in order traversal (left, root, right)
    def inorder_traversal(self, root) : 
        if root is None : 
            return

        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)


    #   post order traversal of a tree (left, right, root)
    def post_order_traversal(self, root) : 
        if root is None : 
            return

        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.data)


    #   iterative pre order traversal
    def iterative_pre_order_traversal(self) : 
        if self.root is None : 
            print('Tree is empty')
            return

        stack = list();root = self.root

        while stack or root : 
            if root is not None : 
                print(root.data)
                stack.append(root)
                root = root.left
            else : 
                root = stack.pop()
                root = root.right      

    
    #   iterative post order traversal left, right, root
    def iterative_inorder(self) : 
        if self.root is None : 
            print('Tree is empty')
            return

        stack = list();pointer = self.root

        while stack or pointer : 
            if pointer is not None : 
                stack.append(pointer)
                pointer = pointer.left
            else : 
                #   before going to right child we print
                pointer = stack.pop()
                pointer = pointer.right


    #   level order traversal
    def levelOrderTraversal(self) :         

        if self.root is None : 
            print('Tree is empty')
            return

        queue = list();root = self.root
        queue.append(root)

        while queue : 
            temp = queue.pop(0)
            if temp.left : 
                print(temp.left.data)
                queue.append(temp.left)
            
            if temp.right : 
                print(temp.right.data)
                queue.append(temp.right)


    #   function to count the number of nodes in the tree
    def count_nodes(self, root) : 
        if root is None : 
            return  0
        else : 
            left_node_sum = self.count_nodes(root.left)
            right_node_sum = self.count_nodes(root.right)
            return left_node_sum + right_node_sum + 1


    #   function to count the number of nodes which has exactly two childs
    def count_even_nodes(self, root) : 
        if root is None : 
            return 0

        else : 
            left_sum = self.count_even_nodes(root.left)
            right_sum = self.count_even_nodes(root.right)

            if root.left and root.right : return left_sum + right_sum + 1
            else : return left_sum + right_sum


    #   function 

    def fun(self, root) : 
        if root is None : 
            return 0
        else : 
            left_sum = self.count_even_nodes(root.left)
            right_sum = self.count_even_nodes(root.right)
            if left_sum > right_sum : return left_sum + 1
            else : return right_sum + 1


    #   function to calculate the number of leaf nodes in a tree
    def count_leaf_nodes(self, root) : 
        if root is None : 
            return 0
        
        left_sum = self.count_leaf_nodes(root.left)
        right_sum = self.count_leaf_nodes(root.right)

        if root.left is None and nroot.right is None : return left_sum + right_sum + 1
        else : return left_sum + right_sum
        
if __name__ == "__main__":
    tree = Tree()
    
    tree.insertNode(1)
    tree.insertNode(2)
    tree.insertNode(3)
    tree.insertNode(4)
    tree.insertNode(5)
    tree.insertNode(6)
    tree.insertNode(7)

    print("Total nodes = {}".format(tree.count_nodes(tree.get_root())))

    print("Total nodes with left and right nodes = {}".format(tree.count_even_nodes(tree.get_root())))

    print("Wahay is : {}".format(tree.fun(tree.get_root())))

    print("number of leaf nodes = {}".format(tree.count_leaf_nodes(tree.get_root())))

    # tree.iterative_pre_order_traversal()

    # print("pre order traversal")
    # tree.preOrderTraversal(tree.get_root())        
    # # print("in order traversal")
    # # tree.inorder_traversal(tree.get_root())
    # print("post order traversal")
    # tree.post_order_traversal(tree.get_root())
    # print('Iterative post order')
    # tree.iterative_inorder()
