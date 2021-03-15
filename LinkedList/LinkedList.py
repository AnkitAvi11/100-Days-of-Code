class Node : 
    def __init__(self, data) : 
        self.data = data
        self.next = None


class LinkedList : 

    def __init__(self) : 
        self.head = None

    
    def createLinkedList(self, data) : 
        new_node = Node(data)
        if self.head is None : 
            self.head = new_node

        else : 
            ptr = self.head
            while ptr.next != None : ptr = ptr.next

            ptr.next = new_node

    
    def traverse(self) : 
        if self.head is None : print("List is empty")
        else : 
            ptr = self.head
            while ptr is not None : 
                print(ptr.data, end = " ")
                ptr = ptr.next

    
    #   function to bring last to the front
    def last_to_front(self) : 
        if self.head is None : return
        ptr = self.head

        while ptr.next.next is not None : ptr = ptr.next

        #   new node
        qptr = Node(ptr.next.data)

        del ptr.next
        ptr.next = None
        qptr.next = self.head
        self.head = qptr


    #   function to remove duplicates from a linked list    
    def remove_duplicates(self) : 
        has_seen = set()
        if self.head is None or self.head.next is None : return []

        ptr = self.head
        has_seen.add(ptr.data)
        qptr = ptr.next

        while qptr is not None : 
            if qptr.data in has_seen : 
                #   delete the node
                dptr = qptr
                qptr = qptr.next
                ptr.next = qptr

                del dptr

                continue

            else : 
                has_seen.add(qptr.data)
            
            #   moving the elements
            ptr = ptr.next
            qptr = qptr.next

    
    #   function to insert a node in a sorted linked list
    def insert_sorted_node(self, data) : 
        new_node = Node(data)

        #   when the list is entirely empty
        if self.head is None : 
            self.head = new_node 
            return data
        
        #   when the list has only one element
        if self.head.next is None : 
            if self.head.data < data : 
                self.head.next = new_node
            else : 
                new_node.next = self.head
                self.head = new_node
            return

        if self.head.data > data : 
            new_node.next = self.head
            self.head = new_node
            return

        #   when the list has some good number of nodes in it
        ptr = self.head
        qptr = ptr.next

        while qptr is not None and qptr.data < data : 
            ptr = ptr.next
            qptr = qptr.next

        new_node.next = qptr
        ptr.next = new_node


    def even_odd(self) : 
        even = list()
        odd = list()

        ptr = self.head

        while ptr is not None : 
            if ptr.data % 2 == 0 : 
                even.append(ptr.data)
            else : 
                odd.append(ptr.data)
            ptr = ptr.next

        new_list = LinkedList()

        even.reverse()

        for el in odd : 
            new_list.createLinkedList(el)
        
        for el in even : 
            new_list.createLinkedList(el)

        self.head = new_list.head


    #   check for palindrome
    def check_for_palindrome(self) : 
        res = list()
        ptr = self.head

        while ptr is not None : 
            res.append(ptr.data)
            ptr = ptr.next

        left = 0;right = len(res) - 1

        while left <= right : 
            if res[left] != res[right] : 
                return False
            left += 1
            right -= 1

        return True

def main() : 
    t = int(input())
    for _ in range(t) : 
        #   input
        n = int(input())
        arr = list(map(int, input().split()))

        #   creating the linked list
        mylist = LinkedList()
        for el in arr : 
            mylist.createLinkedList(el)
        

        # mylist.even_odd()

        print(mylist.check_for_palindrome())

        mylist.traverse()


if __name__ == '__main__' : 
    main()