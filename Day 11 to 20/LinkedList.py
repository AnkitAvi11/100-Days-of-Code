
#   class for creating a individual node
class Node : 

    def __init__(self, sk) : 
        self.data = sk
        self.next = None


#   class for the linkedlist
class LinkedList : 

    #   constructor of the class
    def __init__(self) : 
        self.head = None

    
    #   function to insert a node into the linked list
    def insertNode(self, sk) : 
        new_node = Node(sk)

        #   if the linked list is empty by default (when no nodes are there in the linked list)
        if self.head is None : 
            self.head = new_node

        else : 
            #   if the list contains some nodes
            ptr = self.head 
            while ptr.next is not None : ptr = ptr.next
            ptr.next = new_node

        print('Node added')


    #   function to traverse the entire list
    def traverse(self) : 
        #   if the linked list is empty
        if self.head is None : 
            print('List is empty')
            return
        ptr = self.head
        
        #   traversing the entire linked list
        while ptr is not None : 
            print(ptr.data, end = " : ")
            ptr = ptr.next
        else : 
            print('Complete list printed')

    
    #   function to delete the last node of the linked list
    def deleteLast(self) : 
        
        if self.head is None : 
            print('No element in the linked list')
            return

        ptr = self.head

        #   if the linked list contains a single node
        if ptr.next is None : 
            self.head = None
            data = ptr.data
            del ptr
            return data

        #   if the list contains more than two nodes
        while ptr.next.next is not None : ptr = ptr.next

        qptr = ptr.next

        ptr.next = None;data = qptr.data;del qptr

        return data
