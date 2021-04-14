from tree import Tree 

#   main function for the program
def main() : 
    arr = list(map(int, input().split()))

    tree = Tree()
    for el in arr : 
        tree.createTree(el)

    print("In order traversal = ")
    tree.inOrderTraversal(tree.getRoot())
    


#   driver code for the program
if __name__ == '__main__' : 
    main()